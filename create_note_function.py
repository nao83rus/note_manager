# create_note_function.py Grade 1. Этап 3: Задание 1 Напишите функцию для создания новой заметки и возврата словаря.
from datetime import datetime

# Создаём пустой словарь заметок
notes = {}

# Функция добавления заметки
def create_note(notes):
    # heading = ["username", "title", "description", "status", "created_date", "deadline_date"]
    username = input("ВВведите имя пользователя: ").strip()
    title = input("Введите заголовок заметки: ").strip()
    description = input("Введите описание заметки: ").strip()

    # Запрашиваем ввод статуса и проверяем корректность ввода
    while True:
        status = input("Введите статус заметки (1. новая, 2. в процессе, 3. выполнено): ").strip()
        status = status.lower()
        # Проверяем корректность ввода статуса
        if status == '1' or status.lower() == 'новая':
            status = 'новая'
            break
        elif status == '2' or status.lower() == 'в процессе':
            status = 'в процессе'
            break
        elif status == '3' or status.lower() == 'выполнено':
            status = 'выполнено'
            break
        else:
            print("Введён неверный статус, попробуйте еще раз.")

    # Запрашиваем дату дедлайна и проверяем на корректность
    while True:
        try:
            deadline_tmp = input('Введите дату дедлайна (ГГГГ-ММ-ДД): ')
            if datetime.strptime(deadline_tmp, "%Y-%m-%d"):
                deadline_date = datetime.strptime(deadline_tmp, "%Y-%m-%d").date()
                break
        except ValueError:
            print("Введена некорректная дата, попробуйте ещё раз.")
        except Exception as e:
            # Обработка прочих ошибок
            print(f"Произошла непредвиденная ошибка: {str(e)}")
            print("Пожалуйста, попробуйте снова.")

    # Добавляем текущую дату в качестве даты создания
    created_date = datetime.now().date()

    notes = {"username": username, "title": title,
             "description": description,
             "status": status,
             "created_date": created_date,
             "deadline_date": deadline_date}
    print(type(notes), notes)
    return notes

create_note(notes)
print(type(notes), notes)
# Выводим список созданных заметок на экран
counter = 1
for id, note in notes:
    print(f"Заметка {counter}.")
    print(f"        Имя: {note['username']}")
    print(f"        Заголовок: {note['title']}")
    print(f"        Описание: {note['description']}")
    print(f"        Статус: {note['status']}")
    print(f"        Дата создания: {note['created_date']}")
    print(f"        Дедлайн: {note['deadline_date']}")
    counter = counter + 1
