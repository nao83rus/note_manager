# Grade 1. Этап 2: Задание 5 Удаление заметок
notes = []
heading = ["Имя", "Заголовок", "Комментарий"]

# Добавим несколько заметок
note_data = ["Владимр", "Домашка", "Задание 5"]
note = dict(zip(heading, note_data))
notes.append(note)
note_data = ["Андрей", "Магазин", "Купить молоко"]
note = dict(zip(heading, note_data))
notes.append(note)
note_data = ["Александр", "Тренировка", "Бассейн"]
note = dict(zip(heading, note_data))
notes.append(note)

# Ввыод на экран текущих заметок
def print_notes(notes):
    number = len(notes)
    while number > 0:
        print("Заметка", number)
        number = number - 1
        note_tmp = notes[number]
        print(note_tmp.items())

print_notes(notes)

# Удаление заметок
del_answer = input("Для удаления заметки нажмите 1 или другое, чтобы выйти: ")
if del_answer == "1":
    del_keys = input("Введите значение для поиска и удаления: ")
    # Получим количество элементов списка заметок
    num = len(notes)
    while num > 0:
        num = num - 1
        try:
            # Извлечем словари из списка
            list_tmp = notes[num]
            # Получим значения ключей словаря и проверим на содержание искомой строки
            tmp = list_tmp.values()
            if del_keys in tmp:
                # Нашли искомую строку в значениях ключей, удаляем словарь
                notes.remove(list_tmp)
        except KeyError:
            pass
print_notes(notes)