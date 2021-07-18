# -*- coding: utf-8 -*-
from django.core.cache import cache
from django.core.files.uploadhandler import TemporaryFileUploadHandler


class ProgressBarUploadHandler(TemporaryFileUploadHandler):
    """
    Tracks progress for file uploads.
    The http post request must contain a header or query parameter,
    'X-Progress-ID' which should contain a unique string to identify
    the upload to be tracked.

    Copied from: http://djangosnippets.org/snippets/678/
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.progress_id = None
        self.cache_key = None
        self.original_file_name = None

    def handle_raw_input(self, input_data, META, content_length, boundary,
                         encoding=None):
        """
        Handle the raw input from the client.
        Parameters:
            :input_data:
                An object that supports reading via .read().

            :META:
                ``request.META``.

            :content_length:
                The (integer) value of the Content-Length header from the
                client.

            :boundary: The boundary from the Content-Type header.
                Be sure to prepend two '--'.

        """

        self.content_length = content_length
        if 'X-Progress-ID' in self.request.GET:
            self.progress_id = self.request.GET['X-Progress-ID']
        elif 'X-Progress-ID' in self.request.META:
            self.progress_id = self.request.META['X-Progress-ID']

        if self.progress_id:
            self.cache_key = f"{self.request.META['REMOTE_ADDR']}_"
            "{self.progress_id}"
            cache.set(self.cache_key, {
                'size': self.content_length,
                'received': 0
            }, 30)

    def new_file(self, field_name, file_name, content_type, content_length,
                 charset=None, content_type_extra=None):
        """
        Signal that a new file has been started.
        Warning: As with any data from the client, you should not trust
        content_length (and sometimes won't even get it).
        """
        super().new_file(field_name, file_name, content_type, content_length,
                         charset, content_type_extra)
        self.original_file_name = file_name

    def receive_data_chunk(self, raw_data, start):
        """
        Receive data from the streamed upload parser. ``start`` is the position
        in the file of the chunk. It is called everytime a chunk is received
        """
        super().receive_data_chunk(raw_data, start)
        if self.cache_key:
            data = cache.get(self.cache_key, {})
            data['received'] += self.chunk_size
            cache.set(self.cache_key, data, 30)

        return raw_data
