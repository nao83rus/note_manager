# save_notes_json.py Grade 1. Этап 4: Задание 5 Выбор формата файла
import json

from colorama import init, Fore, Style
init(autoreset=True)

def save_notes_json(notes, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)

    except UnicodeError:
        print(f"{Fore.RED}Не удалось декодировать файл.")
    except PermissionError:
        print(f"{Fore.RED}Ошибка доступа к файлу.")
    except Exception as e:
        print(f"{Fore.RED}Произошла ошибка при записи в файл {e}.")


if __name__ == "__main__":
    notes = [
        {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю',
         'status': 'новая', 'created_date': '2025-1-10', 'issue_date': '2025-1-30'},
        {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену',
         'status': 'в процессе', 'created_date': '2025-2-10', 'issue_date': '2025-2-20'},
        {'username': 'Игорь', 'title': 'Спорт', 'content': 'Подготовиться к соревнованиям',
         'status': 'в процессе', 'created_date': '2025-2-10', 'issue_date': '2025-2-20'},
    ]
    save_notes_json(notes, 'netes.json')