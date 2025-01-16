# update_note_function.py Grade 1. Этап 3: Задание 2 Функция обновления заметки
from datetime import date

from test_file import heading

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

for index, note in enumerate(notes, start= 1):
     print(f" \nЗаметка номер {index}")
     for key, value in note.items():
          print(f"{key}: {value}")
# Получаем номер заметки для изменения
note_number = input(f"\n Какую заметку будем менять? Введите номер: ")

# Получаем поле для изменения
field = input(f"выберите поле для обновления: ")
# Функция обновления заметки
def update_note():
    pass