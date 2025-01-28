 # setup_database.py Grade 1. Этап 6: Задание 1 Работа с базами данных
import sqlite3
# from tkinter.constants import INSERT

def setup_database(notes):
    # Создаём подключение к БД
    connection = sqlite3.connect("notes.db")
    # Создаем курсор
    cursor = connection.cursor()
    # Создаем таблицу БД
    cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        status TEXT NOT NULL,
        created_date TEXT NOT NULL,
        issue_date TEXT NOT NULL)
         ''')
    # Наполняем таблицу БД данными
    for note in notes:
        cursor.execute("""
            INSERT INTO notes (username, title, content, status, created_date, issue_date)
            VALUES (?, ?, ?, ?, ?, ?);
        """, (
        note['username'], note['title'], note['content'], note['status'], note['created_date'], note['issue_date']))
        # Сохраняем изменения
        connection.commit()
    # Закрываем БД
    connection.close()

if __name__ == "__main__":

    notes = [
        {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю',
         'status': 'новая', 'created_date': '2025-1-10', 'issue_date': '2025-1-30'},
        {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену',
         'status': 'в процессе', 'created_date': '2025-2-10', 'issue_date': '2025-2-20'},
        {'username': 'Игорь', 'title': 'Спорт', 'content': 'Подготовиться к соревнованиям',
         'status': 'в процессе', 'created_date': '2025-2-10', 'issue_date': '2025-2-20'},
    ]

    setup_database(notes)