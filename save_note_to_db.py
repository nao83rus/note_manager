# save_note_to_db Grade 1. Этап 6: Задание 2 Сохранение заметок в базу данных

def save_note_to_db(note, db_path):

    import sqlite3
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO notes (username, title, content, status, created_date, issue_date)
        VALUES (?, ?, ?, ?, ?, ?);
    """, (note['username'], note['title'], note['content'], note['status'], note['created_date'], note['issue_date']))
    connection.commit()

    connection.close()

if __name__ == "__main__":

    note = {'username': 'Владимир', 'title': 'Skill Place', 'content': 'Подать заявление',
         'status': 'новая', 'created_date': '2025-1-31', 'issue_date': '2025-2-3'}

    save_note_to_db(note, "notes.db")