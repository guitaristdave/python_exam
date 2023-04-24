from Note import Note
import json

class Notes:
    def __init__(self, filename):
        self.filename = filename
        self.notes = []
        self.load()

    def load(self):
        try:
            with open(self.filename) as f:
                notes_data = json.load(f)
                self.notes = [Note(n['id'], n['title'], n['body']) for n in notes_data]
        except FileNotFoundError:
            pass

    def save(self):
        with open(self.filename, 'w') as f:
            notes_data = [note.get_info() for note in self.notes]
            json.dump(notes_data, f)

    def add(self, title, body):
        note = Note(len(self.notes) + 1, title, body)
        self.notes.append(note)
        self.save()

    def read(self, id):
        for note in self.notes:
            if note.id == id:
                return note.get_info()
        return None

    def edit(self, id, title, body):
        for note in self.notes:
            if note.id == id:
                note.edit(title, body)
                self.save()
                return
        raise ValueError(f'Note with id {id} not found')

    def delete(self, id):
        for note in self.notes:
            if note.id == id:
                self.notes.remove(note)
                self.save()
                return
        raise ValueError(f'Note with id {id} not found')
