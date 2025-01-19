# update_note_function.py Grade 1. Этап 3: Задание 2 Функция обновления заметки
import datetime
from datetime import date

# Функция обновления заметки
def update_note(editable_note):
    # Список полей (ключей в словаре)
    list_key = []
    while True:
        # Получаем поле для изменения
        field = input(f"выберите поле для обновления: ")
        current_key = list(editable_note.keys())
        if field not in current_key:
            print("Выбрано неверное поле. Попробуйте еще раз")
        else:
            break

    # Получим новое значение поля
    while True:
        field_value = input(f"Введите новое значение поля {field}: ").lower().strip()
        # Проверим поля ststus и issue_date на корректность
        if field == 'status':
            if field_value == 'новая' or field_value == 'в процессе' or field_value == 'отложено':
                editable_note[field] = field_value.strip()
                break
            else:
                print("Введено неверное значение статуса. Введите: новая/в процессе/отложено.")
        elif field == 'issue_date':
            try:
                datetime.datetime.strptime(field_value, '%Y-%m-%d')
                editable_note[field] = field_value
                return True
            except ValueError:
                print("Введено неверное значение даты. Введите: ГГГГ-ММ-ДД")
                # return False
        else:
            editable_note[field] = field_value
            break

    print("\nОтредактированная заметка:")
    for key, value in editable_note.items():
        print(f"{key}: {value}")
    # return editable_note

if __name__ == "__main__":
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
    # Покажем имеющиеся заметки
    print("Имеются следующие заметки:")
    for index, note in enumerate(notes, start= 1):
        print(f" \nЗаметка номер {index}")
        for key, value in note.items():
              print(f"{key}: {value}")

    # Получаем заметку для изменения
    while True:
        note_number = int(input(f"\nКакую заметку будем менять? Введите номер: "))-1
        # Проверяем корректность ввода номера заметки
        if 0 <= note_number < len(notes):
            editable_note = notes[note_number]
            break
        else:
            print("Введено неверное значение. Попробуйте еще раз.")

    update_note(editable_note)