# Grade 1. Этап 2: Задание 5 Удаление заметок
notes = []
heading = ["name", "content", "description"]

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

# while True:
#     answer = input("Для добавления следующей заметки введите 1 или другое для прекращения: ")
#     if answer == "1":
#         name = input("Введите имя: ")
#         title = input("Введите заголовок: ")
#         description = input("Введите описание: ")
#         note_data = [name, title, description]
#         notes.append(dict(zip(note_title, note_data)))
#     else:
#         break
# number = 0
# for note_number in notes:
#     number = number + 1
#     print(notes)

# Удаление заметок
del_answer = input("Для удаления заметки нажмите 1 или другое, чтобы выйти: ")
if del_answer == "1":
    del_keys = "Владимр" #input("Введите значение для поиска и удаления: ")
    # notes.remove(del_keys)
    num = len(notes)
    while num > 0:
        num = num - 1
        try:
            list_tmp = notes[num]
            tmp = list_tmp.values()
            if del_keys in tmp:
                notes.remove(list_tmp)
            # print(notes[num])
        except KeyError:
            pass
print(notes)