# load_notes_from_db Grade 1. Этап 6: Задание 3 Загрузка заметок из базы данных

def load_notes_from_db(db_path):
    import sqlite3
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM notes;")
    rows = cursor.fetchall()
    notes = []

    for row in rows:
        notes.append({
            'id': row[0],
            'username': row[1],
            'title': row[2],
            'content': row[3],
            'status': row[4],
            'created_date': row[5],
            'issue_date': row[6],
        })
    connection.close()
    return notes

if __name__ == "__main__":

    notes = (load_notes_from_db("notes.db"))
    print(notes)