# update_note_function.py Grade 1. Этап 3: Задание 2 Функция обновления заметки
from datetime import date

# Предопределим список заметок
notes = [
    {
        'username': 'Алексей',
        'title': 'Список покупок',
        'content': 'Купить продукты на неделю',
        'status': 'новая',
        'issue_date': date(2025,1,19)
    },
    {
        'username': 'Мария',
        'title': 'Учеба',
        'content': 'Подготовиться к экзамену',
        'status': 'новая',
        'issue_date': date(2025,1,20)
    },
    {
        'username': 'Алексей',
        'title': 'Встреча',
        'content': 'Встреча с друзьями',
        'status': 'новая',
        'issue_date': date(2025,1,21)
    }
]

# Функция обновления заметки
def update_note(editable_note):
    # Список полей (ключей в словаре)
    list_key = []
    while True:
        # Получаем поле для изменения
        field = input(f"выберите поле для обновления: ")
        for note in notes:
            current_key = note.keys()
            for key in current_key:
                list_key.append(key)
            break
        # Проверяем корректность ввода поля для изменения
        if field not in list_key:
            # Нет такого поля (ключа) - запрашиваем еще раз
            print("Выбрано неверное поле. Попробуйте еще раз")
        else:
            break

    # Получим новое значение поля
    field_value = input(f"Введите новое значение поля {field}: ")

    editable_note[field] = field_value
    return editable_note

# Покажем имеющиеся заметки
for index, note in enumerate(notes, start= 1):
    print(f" \nЗаметка номер {index}")
    for key, value in note.items():
          print(f"{key}: {value}")

# Получаем заметку для изменения
while True:
    tmp_number = int(input(f"\nКакую заметку будем менять? Введите номер: "))
    # Проверяем корректность ввода номера заметки
    if tmp_number >= 0 and tmp_number <= notes.__len__():
        note_number = tmp_number - 1
        editable_note = notes[note_number]
        break
    else:
        print("Введено неверное значение. Попробуйте еще раз.")

update_note(editable_note)
print("\nОтредактированная заметка:")
for key, value in editable_note.items():
    print(f"{key}: {value}")

for index, note in enumerate(notes, start= 1):
    print(f" \nЗаметка номер {index}")
    for key, value in note.items():
          print(f"{key}: {value}")
