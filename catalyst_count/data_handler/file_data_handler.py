from io import StringIO
import pandas as pd
from django_q.tasks import async_task
from .chunk_process import save_chunk


def get_dataframe_from_csv(uploaded_file, chunk_size=10**6):
    cols = []
    remaining = ""
    for idx, chunk in enumerate(uploaded_file.chunks(chunk_size)):
        content = chunk.decode(errors="replace")
        content = remaining + content
        last_line_idx = content.rfind("\n")
        remaining = content[last_line_idx+1:]
        if content[-1] == "\n":
            remaining = ""
        content = content[:last_line_idx]
        file = StringIO(content)
        df = pd.read_csv(file, index_col=0,
                         header=0 if len(cols) == 0 else None,
                         names=None if len(cols) == 0 else cols)
        if len(cols) == 0:
            cols = df.columns.to_list()
        yield df


def handle_uploaded_file(uploaded_file):
    for df in get_dataframe_from_csv(uploaded_file):
        async_task(save_chunk, df, group="file_upload_chunk")
