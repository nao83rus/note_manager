# search_notes_function.py Grade 1. Этап 3: Задание 4 Функция поиска заметок
import datetime
from datetime import date
from colorama import init, Fore, Style

def search_notes(notes, keyword=None, status=None):
    fields_for_search = ["title", "content", "username"]

    for note in notes:
        keyword_creteria = True
        status_creteria = True

        # if keyword != None: # сравнение по значение
        if keyword is not None:  # сравнение по ссылки (объект один и тот же)
            for field in fields_for_search:

                # print("keyword: ",keyword, type(keyword))
                # print("value: ",note[field].lower(), type(note[field].lower()))
                # if note[field].lower() == keyword:
                if keyword in note[field].lower().strip():
                    keyword_creteria = True
                    break
                else:
                    keyword_creteria = False
        if status is not None:
            if note["status"].strip() == status:
                status_creteria = True
            else:
                status_creteria = False

        if keyword_creteria == True and status_creteria == True:
            found_notes.append(note)
    # Возвращаем список найденных заметок
    return found_notes
if __name__ == '__main__':

    # Предопределённый список заметок
    notes = [
        {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю',
            'status': 'новая', 'created_date': date(2025, 1, 10), 'issue_date': date(2025, 1, 30)},
        {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену',
            'status': 'новая', 'created_date': date(2025, 1, 9), 'issue_date': date(2025, 2, 20)},
        {'username': 'Игорь', 'title': 'Учеба', 'content': 'Подготовиться к экзамену',
            'status': 'отложена', 'created_date': date(2025, 1, 10), 'issue_date': date(2025, 2, 25)},
        {'username': 'Мария', 'title': 'Учеба', 'content': 'Сдать задание',
            'status': 'новая', 'created_date': date(2025, 1, 18), 'issue_date': date(2025, 1, 20)},
        {'username': 'Игорь', 'title': 'Спорт', 'content': 'Подготовиться к соревнованиям',
            'status': 'новая', 'created_date': date(2025, 1, 30), 'issue_date': date(2025, 2, 28)},
        {'username': 'Илья', 'title': 'Авто', 'content': 'Помыть машину',
            'status': 'новая', 'created_date': date(2025, 1, 20), 'issue_date': date(2025, 2, 21)},
        {'username': 'Стас', 'title': 'Авто', 'content': 'Заменить масло в двигателе',
            'status': 'в процессе', 'created_date': date(2025, 1, 16), 'issue_date': date(2025, 1, 23)},
        {'username': 'Алексей', 'title': 'Встреча', 'content': 'Встреча с друзьями',
            'status': 'выполнена', 'created_date': date(2025, 1, 8), 'issue_date': date(2025, 1, 21)}
    ]
    found_notes = [] # список с найденными заметками
    keyword = input("Введите слово или его часть для поиска в полях Имя, Заголовок, Описание: ").lower().strip()
    if keyword == '':
        keyword = None
    status = input("Введите статус для поиска: ").lower().strip()
    if status == '':
        status = None
    search_notes(notes, keyword, status)

    if found_notes.__len__() == 0:
        print(f"{Fore.BLUE}Список найденных заметок пуст:")
    else:
        print(f"{Fore.BLUE}Список найденных заметок:")
    counter = 1
    for note in found_notes:
        print(f"""{Fore.LIGHTCYAN_EX}Заметка {counter}.
        {Fore.GREEN}Имя пользователя: {note['username']}
        {Fore.YELLOW}Заголовок: {note['title']}
        {Fore.MAGENTA}Описание: {note['content']}
        {Fore.BLUE}Статус: {note['status']}
        {Fore.LIGHTCYAN_EX}Дата создания: {note['created_date']}
        {Fore.RED}Дедлайн: {note['issue_date']}
        {Fore.LIGHTGREEN_EX}_______________________________________________""")
        counter = counter + 1
