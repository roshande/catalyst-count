import pandas as pd
from .models import Companies
from django_q.tasks import async_task, result

def handle_uploaded_file(uploaded_file):
    csv_data = pd.read_csv(uploaded_file)
    column_renames = {
        "size range": "size_range", "year founded": "year_founded",
        "linkedin url": "linkedin_url",
        "current employee estimate": "current_employee_estimate",
        "total employee estimate": "total_employee_estimate"
    }
    csv_data = csv_data.rename(columns=column_renames)
    records = csv_data.to_dict(orient="records")
    Companies.obj.bulk_create(records, 100)




