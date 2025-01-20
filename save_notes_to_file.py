# save_notes_to_file.py Grade 1. Этап 4: Задание 1 Сохранение заметок в файл
from datetime import date

def save_notes_to_file(notes, filename):
    # Открываем файл для записи
    # file = open(filename, 'w', encoding='utf-8')
    with open(filename, 'w', encoding='utf-8') as file:  # 'w' — создаем файл если нету, и перезаписыавем содержимое

        # for note in notes:
        #     file.write('___________________________\n')
        #     for key, value in note.items():
        #         file.write(f"{key}: {value}\n")

        for note in notes:
            file.write(f"Имя пользователя: {note['username']}\n")
            file.write(f"Заголовок: {note['title']}\n")
            file.write(f"Описание: {note['content']}\n")
            file.write(f"Статус: {note['status']}\n")
            file.write(f"Дата создания: {note['created_date']}\n")
            file.write(f"Дедлайн: {note['issue_date']}\n")
            file.write(f"_______________________________________________\n")

    # file.close()



if __name__ == "__main__":
    notes = [
        {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю',
         'status': 'новая', 'created_date': date(2025, 1, 10), 'issue_date': date(2025, 1, 30)},
        {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену',
         'status': 'в процессе', 'created_date': date(2025, 1, 9), 'issue_date': date(2025, 2, 20)},
        {'username': 'Игорь', 'title': 'Учеба', 'content': 'Подготовиться к экзамену',
         'status': 'отложена', 'created_date': date(2025, 1, 10), 'issue_date': date(2025, 2, 25)},
        {'username': 'Мария', 'title': 'Учеба', 'content': 'Сдать задание',
         'status': 'новая', 'created_date': date(2025, 1, 18), 'issue_date': date(2025, 1, 20)},
        {'username': 'Игорь', 'title': 'Спорт', 'content': 'Подготовиться к соревнованиям',
         'status': 'отложена', 'created_date': date(2025, 1, 30), 'issue_date': date(2025, 2, 28)},
        {'username': 'Илья', 'title': 'Авто', 'content': 'Помыть машину',
         'status': 'новая', 'created_date': date(2025, 1, 20), 'issue_date': date(2025, 2, 21)},
        {'username': 'Стас', 'title': 'Авто', 'content': 'Заменить масло в двигателе',
         'status': 'в процессе', 'created_date': date(2025, 1, 16), 'issue_date': date(2025, 1, 23)},
        {'username': 'Алексей', 'title': 'Встреча', 'content': 'Встреча с друзьями',
         'status': 'выполнена', 'created_date': date(2025, 1, 8), 'issue_date': date(2025, 1, 21)}
    ]

save_notes_to_file(notes, 'notes.txt')
