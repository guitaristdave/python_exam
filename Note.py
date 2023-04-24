import datetime
import json

class Note:
    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def get_info(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    def edit(self, title, body):
        self.title = title
        self.body = body
        self.updated_at = datetime.datetime.now()
