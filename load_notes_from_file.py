# load_notes_from_file.py Grade 1. Этап 4: Задание 2 Загрузка заметок из файла
from colorama import init, Fore, Style
from transliterate import translit
init(autoreset=True)

def load_notes_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        # Читаем файл построчно
        lines = file.readlines()
        # Проверяем, не пустой ли файл
        if len(lines) > 0:
            # инициализируем пустой словарь
            note = {}
            # итерируем по каждой строке и разбиваем пары ключ-значение
            for line in lines:
                # Проверяем на разделитель заметок, если есть - добавляем в словарь
                if '__' in line:
                    notes.append(note)
                # Проверяем ':' если его нет - пропускаем выполнение
                elif ':' not in line:
                    continue
                else:
                    # разделяем каждую строку по двоеточию
                    key, value = line.strip().split(':')
                    # Транслитирируем кириллицу в латиницу
                    key = translit(key.lower(), language_code='ru', reversed=True)
                    # В ключе вместо пробела поставим '_'
                    key = key.replace(' ', '_')
                    # добавляем в словарь
                    note[key.strip()] = value.strip()
        else:
            print(f"{Fore.RED}Файл {filename} пуст.")

    return notes

if __name__ == "__main__":
    notes = []
    load_notes_from_file("notes.txt")

    counter = 1
    for note in notes:
        for key, value in note.items():
            print(f"{key}: {value}")
            counter += 1