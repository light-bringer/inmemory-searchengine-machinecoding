import datetime
import uuid


class Document:

    def __init__(self, doc_id: int, content):
        self.doc_id = doc_id
        self.content = content
        self.created_at = datetime.datetime.now()

    def get_id(self):
        return self.doc_id

    def get_content(self):
        return self.content

    def creation_date(self):
        return self.created_at
