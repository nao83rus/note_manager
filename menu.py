# menu.py Grade 1. Этап 3: Задание 5 Меню действий
from datetime import date
from colorama import init, Fore, Style

from create_note_function import create_note
from update_note_function import update_note
from display_notes_function import display_notes
from search_notes_function import search_notes

# Инициализация библиотеки
init(autoreset=True)

def delete_note(notes):
    if notes:
        display_notes(notes)
        index = int(input("Введите номер заметки для обновления: ")) - 1
        if 0 <= index < len(notes):
            answer_del = input(f"Вы действительно хотите удалить заметку {index+1} (да/нет)").strip().lower()
            if answer_del == "да":
                del_notes = notes.pop(index)
                print(del_notes)
                print(f'Введено "{answer_del}".')
            else:
                print(f'Введено "{answer_del}". Заметка не удалена.')
                return
        else:
            print("Неверный номер заметки.")
    else:
        print("Список заметок пуст.")
    print(f"Удалена заметка номер {index+1}")
    print(f"{Fore.GREEN} Имя пользователя: {del_notes['username']}")
    print(f"{Fore.YELLOW} Заголовок: {del_notes['title']}")
    print(f"{Fore.MAGENTA} Описание: {del_notes['content']}")
    print(f"{Fore.BLUE} Статус: {del_notes['status']}")
    print(f"{Fore.LIGHTCYAN_EX} Дата создания: {del_notes['created_date']}")
    print(f"{Fore.RED} Дедлайн: {del_notes['issue_date']}")
    print(f"{Fore.LIGHTGREEN_EX}_______________________________________________")
    return notes

def display_menu(notes):
    while True:
        # Отобразить меню
        print(f"{Fore.GREEN}\nМеню действий:")
        print(f"{Fore.BLUE}1. Создать новую заметку")
        print(f"{Fore.YELLOW}2. Показать все заметки")
        print(f"{Fore.RED}3. Обновить заметку")
        print(f"{Fore.CYAN}4. Удалить заметку")
        print(f"{Style.BRIGHT}{Fore.MAGENTA}5. Найти заметки")
        print("6. Выйти из программы")

        try:
            choice = input("Ваш выбор: ")
            if choice == "1":
                note = create_note(notes)
                notes.append(note)
            elif choice == "2":
                display_notes(notes)
            elif choice == "3":
                if notes:
                    display_notes(notes)
                    index = int(input("Введите номер заметки для обновления: ")) - 1
                    if 0 <= index < len(notes):
                        notes[index] = update_note(notes[index])
                    else:
                        print("Неверный номер заметки.")
                else:
                    print("Список заметок пуст.")
            elif choice == "4":
                notes = delete_note(notes)
            elif choice == "5":
                keyword = input("Введите слово или его часть для поиска в полях Имя, Заголовок, Описание: ").lower().strip()
                if keyword == '':
                    keyword = None
                # Запрашиваем статус и проверяем на корректность ввода
                while True:
                    status = input("Введите статус для поиска (новая/в процессе/отложена/выполнена или оставьте пустым): ").lower().strip()
                    if status == '':
                        status = None
                        break
                    elif status == 'новая' or status == 'в процессе' or status == 'отложена' or status == 'выполнена':
                        break
                    else:
                        print("Введено неверное значение. Попробуйте ещё раз.")
                search_notes(notes, keyword, status)
            elif choice == "6":
                print("Программа завершена. Спасибо за использование!")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
        except ValueError:
            print("Ошибка: введите число от 1 до 6.")

# Запуск меню
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
    display_menu(notes)
