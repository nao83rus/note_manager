# Импортируем наши модули
# Из Data
from data.append_notes_to_file import append_notes_to_file
from data.load_notes_from_file import load_notes_from_file
from data.save_notes_json import save_notes_json
from data.save_notes_to_file import save_notes_to_file
# Из Interface
from interface.display_notes_function import display_notes
from interface.menu import display_menu
# Из Tests
import tests.test_save_and_load_note
# Из Utils
from utils.date_validator import validate_date
from utils.status_validator import validate_status
from utils.uuid_generator import generate_unique_id

def main_menu():
    while True:
        # Отобразить меню
        print(f"\nМеню действий:")
        print(f"1. Добаить заметку файл")
        print(f"2. Загрузить заметки из файла")
        print(f"3. Сохранить заметки в файл txt")
        print(f"4. Сохранить заметки в файл json")
        print(f"5. Вывести список заметок")
        print(f"6. Проверка даты")
        print(f"7. Проверка статуса")
        print(f"8. Генерировать ID заметки")
        print(f"9. Вывести ещё меню")
        print(f"0. Выйти из программы")

        try:
            choice = input("Ваш выбор: ")
            if choice == "1":
                append_notes_to_file(notes, "main.txt")
            elif choice == "2":
                load_notes_from_file("main.txt")
            elif choice == "3":
                save_notes_to_file(notes,"main.txt")
            elif choice == "4":
                save_notes_json(notes, "main.json")
            elif choice == "5":
                display_notes(notes)
            elif choice == "6":
                date_str = input("Введите дату в формате ГГГГ-ММ-ДД: ")
                print(validate_date(date_str))
            elif choice == "7":
                status_str = input("Введите статус: ")
                print(validate_status(status_str))
            elif choice == "8":
                print(generate_unique_id())
            elif choice == "9":
                display_menu(notes)
            elif choice == "0":
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
        except ValueError:
            print("Ошибка: введите число от 0 до 9.")

if __name__ == "__main__":
    notes = [
        {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю',
         'status': 'новая', 'created_date': '2025-1-10', 'issue_date': '2025-1-30'},
        {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену',
         'status': 'в процессе', 'created_date': '2025-2-10', 'issue_date': '2025-2-20'},
        {'username': 'Игорь', 'title': 'Спорт', 'content': 'Подготовиться к соревнованиям',
         'status': 'в процессе', 'created_date': '2025-2-10', 'issue_date': '2025-2-20'},
    ]
    main_menu()