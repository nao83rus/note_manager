# append_notes_to_file.py Grade 1. Этап 4: Задание 4 Добавление данных в файл
from transliterate import translit
from colorama import init, Fore, Style
init(autoreset=True)

def load_notes_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            # Читаем файл построчно
            lines = file.readlines()
            # Проверяем, не пустой ли файл
            if len(lines) > 0:
                # инициализируем пустой словарь
                note = {}
                # инициализируем список ключей
                note_key = []
                # итерируем по каждой строке и разбиваем пары ключ-значение
                for line in lines:
                    # Проверяем на разделитель заметок, если есть - добавляем в словарь
                    if ':' in line:
                        # разделяем каждую строку по двоеточию
                        key, value = line.strip().split(':')
                        if key not in note_key:
                            # Добавим ключ в список ключей для отслеживания повторений
                            note_key.append(key)
                            # Транслитирируем кириллицу в латиницу
                            key = translit(key.lower(), language_code='ru', reversed=True)
                            # В ключе вместо пробела поставим '_'
                            key = key.replace(' ', '_')
                            # добавляем в словарь
                            note[key.strip()] = value.strip()
                        else:
                            # Такой ключ уже есть. Добавляем словарь в список и очищаем список ключей
                            note_key = []
                            notes.append(note)
            else:
                print(f"{Fore.RED}Файл {filename} пуст.")
    except FileNotFoundError:
        file = open(filename,mode='w', encoding='utf-8')
        file.close()
        print(f"{Fore.RED}Файл не найден. Создали новый файл.")
    except UnicodeError:
        print(f"{Fore.RED}Не удалось декодировать файл.")
    except PermissionError:
        print(f"{Fore.RED}Ошибка доступа к файлу.")
    return notes

if __name__ == "__main__":
    notes = []
    load_notes_from_file("notes.txt")

    counter = 1
    for note in notes:
        for key, value in note.items():
            print(f"{key}: {value}")
            counter += 1