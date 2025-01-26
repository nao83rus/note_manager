# load_notes_from_file.py Grade 1. Этап 4: Задание 2: Загрузка заметок из файла
from colorama import init, Fore, Style
init(autoreset=True)
notes = []
def load_notes_from_file(filename):
    # инициализируем пустой словарь
    note = {}
    # инициализируем список ключей
    note_key = []
    # Словарь транслитерации ключей
    translate_table = {
        "Имя пользователя": "username",
        "Заголовок": "title",
        "Описание": "content",
        "Статус": "status",
        "Дата создания": "created_date",
        "Дедлайн": "issue_date"
    }
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            # Читаем файл построчно
            lines = file.readlines()
            # Проверяем, не пустой ли файл
            if len(lines) > 0:
                number_note = 0
                # итерируем по каждой строке и разбиваем пары ключ-значение
                for line in lines:
                    # Проверяем на разделитель заметок, если есть - добавляем в словарь
                    if ':' in line:
                        # разделяем каждую строку по двоеточию
                        verbose_key, value = line.strip().split(':')
                        if verbose_key not in note_key:
                            # Добавим ключ в список ключей для отслеживания повторений
                            note_key.append(verbose_key)
                            # Попытка: Если проверяемый ключ отсутствует, его не будем транслитерировать и запишем как есть
                            try:
                                key = translate_table[verbose_key]
                                note[key.strip()] = value.strip()
                            except Exception:
                                # Если ключ записан на английском - оставляем его как есть
                                note[verbose_key.strip()] = value.strip()
                        else:
                            # Такой ключ уже есть. Добавляем словарь в список и очищаем список ключей
                            notes.append(note)
                            note_key = []
                            # Увеличиваем номер заметки
                            number_note += 1
            else:
                print(f"{Fore.RED}Файл {filename} пуст.")
            # Если у нас одна заметка, не будет повторения ключей и она не добавится в список. Исправляем так.
            if number_note == 0:
                notes.append(note)
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

    load_notes_from_file("notes.txt")
    # Выводим наши заметки на экран
    counter = 1
    for note in notes:
        for key, value in note.items():
            print(f"{key}: {value}")
            counter += 1