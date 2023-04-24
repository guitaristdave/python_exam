from Notes import Notes
from NotesApp import NotesApp

if __name__ == '__main__':
    notes = Notes('notes.json')  # создаем объект класса Notes и указываем файл для сохранения заметок
    app = NotesApp(notes)  # передаем объект класса Notes в качестве аргумента при создании объекта класса NotesApp
    app.run()  # запускаем приложение
