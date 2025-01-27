# display_notes_function.py Grade 1. Этап 3: Задание 3 Функция отображения заметок
import datetime
from datetime import date
from colorama import init, Fore, Style
from textwrap import dedent

# Инициализация библиотеки colorama
init(autoreset=True)

def display_notes(notes):
    answer_sort = input("Сделать сортировку по дате дедлайна (да / (нет или оставьте поле пустым)?")
    if answer_sort == 'да':
        sorted_notes = sorted(notes, key=lambda x: x['issue_date'])
        notes = sorted_notes
    # Выводим список заметок на экран
    # Если список заметок пуст - выводим об этом сообщение
    while True:
        answer = int(input('''Как вы хотите просмотреть заметки (1/2):
        1. Только заголовки с дедлайном
        2. Полные заметки
        '''))
        if answer == 2:
            if len(notes) == 0:
                print("У вас нет сохранённых заметок.")
            else:
                print("Список заметок:")
                counter = 1
                for note in notes:
                    massege = (f"""
                    Заметка {counter}.
                    {Fore.GREEN}Имя пользователя: {note['username']}
                    {Fore.YELLOW}Заголовок: {note['title']}
                    {Fore.MAGENTA}Описание: {note['content']}
                    {Fore.BLUE}Статус: {note['status']}
                    {Fore.LIGHTCYAN_EX}Дата создания: {note['created_date']}
                    {Fore.RED}Дедлайн: {note['issue_date']}
                    {Fore.LIGHTGREEN_EX}_______________________________________________""")
                    print(dedent(massege))
                    counter = counter + 1
            break
        elif answer == 1:
            print("Список заголовков заметок с дедлайном:")
            counter = 1
            for note in notes:
                massege = (f"""
                Заметка {counter}.
                {Fore.RED}Заголовок: {note['title']}
                {Fore.GREEN}Дедлайн: {note['issue_date']}
                {Fore.BLUE}_______________________________________________""")
                print(dedent(massege))
                counter = counter + 1
            break
        else:
            print("Введено неверное значение. Попробуйте ещё раз")
    return notes

if __name__ == "__main__":
    # Предопределённый список заметок
    notes = [
        {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю',
         'status': 'новая', 'created_date': '2025-1-10', 'issue_date': '2025-1-30'},
        {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену',
         'status': 'в процессе', 'created_date': '2025-2-10', 'issue_date': '2025-2-20'},
        {'username': 'Игорь', 'title': 'Спорт', 'content': 'Подготовиться к соревнованиям',
         'status': 'в процессе', 'created_date': '2025-2-10', 'issue_date': '2025-2-20'},
    ]

    display_notes(notes)