from Notes import Notes  # импортируем класс Notes из notes.py

class NotesApp:
    def __init__(self, notes):
        self.notes = notes  # принимаем объект класса Notes

    def run(self):
        while True:
            # выводим доступные команды
            print('Доступные команды: add, read, edit, delete, list, quit')
            command = input('Введите команду (add/read/edit/delete/list/quit): ')

            if command == 'add':
                title = input('Введите заголовок: ')
                body = input('Введите текст заметки: ')
                self.notes.add(title, body)  # вызываем метод add из класса Notes
                print('Заметка успешно добавлена')

            elif command == 'read':
                id = int(input('Введите ID заметки: '))
                note = self.notes.read(id)  # вызываем метод read из класса Notes
                if note:
                    print(note)
                else:
                    print(f'Заметка с ID {id} не найдена')

            elif command == 'edit':
                id = int(input('Введите ID заметки: '))
                title = input('Введите новый заголовок: ')
                body = input('Введите новый текст заметки: ')
                try:
                    self.notes.edit(id, title, body)  # вызываем метод edit из класса Notes
                    print(f'Заметка с ID {id} успешно изменена')
                except ValueError as e:
                    print(str(e))

            elif command == 'delete':
                id = int(input('Введите ID заметки: '))
                try:
                    self.notes.delete(id)  # вызываем метод delete из класса Notes
                    print(f'Заметка с ID {id} успешно удалена')
                except ValueError as e:
                    print(str(e))

            elif command == 'list':
                for note in self.notes.notes:
                    print(note.get_info())  # выводим информацию о заметках с помощью метода get_info

            elif command == 'quit':
                break

            else:
                print('Некорректная команда')

