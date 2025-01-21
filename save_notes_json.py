# save_notes_json.py Grade 1. Этап 4: Задание 5 Выбор формата файла

from colorama import init, Fore, Style
init(autoreset=True)

def save_notes_json(notes, filename):
    try:
        pass

    except FileNotFoundError:
        file = open(filename, mode='w', encoding='utf-8')
        file.close()
        print(f"{Fore.RED}Файл не найден. Создали новый файл.")
    except UnicodeError:
        print(f"{Fore.RED}Не удалось декодировать файл.")
    except PermissionError:
        print(f"{Fore.RED}Ошибка доступа к файлу.")


if __name__ == "__main__":
    pass