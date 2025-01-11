# Grade 1. Этап 2: Задание 4 Реализуем возможность создания и хранения нескольких заметок в списке.
from datetime import datetime

# Создаём пустой список заметок
notes = []
while True:
    # Спрашиваем, хочет ли пользователь добавить заметку.
    answer = input('Создать заметку? (введите: "1", "да" или "yes", чтобы создать. Или другое для выхода).\n')
    # Если ответ положительный - создаем заметку
    if answer.lower() == 'да' or answer.lower() == 'yes' or answer == '1':
        heading = ["username", "content", "description", "status", "created_date", "deadline_date"]
        username = input("ВВведите имя пользователя: ")
        content = input("Введите содержание заметки: ")
        description = input("Введите описание заметки: ")
        while True:
            status = input("Введите статус заметки (1. новая, 2. в процессе, 3. выполнено): ")
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
        while True:
            try:
                created_tmp = input('Введите дату создания (ДД-ММ-ГГГГ или ГГГГ-ММ-ДД): ')
                if created_tmp[5] == '-':
                    if datetime.strptime(created_tmp, "%d-%m-%Y"):
                        created_date = datetime.strptime(created_tmp, "%d-%m-%Y")
                        break
                if created_tmp[7] == '-':
                    if datetime.strptime(created_tmp, "%Y-%m-%d"):
                        created_date = datetime.strptime(created_tmp, "%Y-%m-%d")
                        break
            except ValueError:
                print("Введена некорректная дата, попробуйте ещё раз.")
            except Exception as e:
                # Обработка прочих ошибок
                print(f"Произошла непредвиденная ошибка: {str(e)}")
                print("Пожалуйста, попробуйте снова.")
        while True:
            try:
                deadline_tmp = input('Введите дату создания (ДД-ММ-ГГГГ или ГГГГ-ММ-ДД): ')
                if deadline_tmp[5] == '-':
                    if datetime.strptime(deadline_tmp, "%d-%m-%Y"):
                        deadline_date = datetime.strptime(deadline_tmp, "%d-%m-%Y")
                        break
                if created_tmp[7] == '-':
                    if datetime.strptime(deadline_tmp, "%Y-%m-%d"):
                        deadline_date = datetime.strptime(deadline_tmp, "%Y-%m-%d")
                        break
            except ValueError:
                print("Введена некорректная дата, попробуйте ещё раз.")
            except Exception as e:
                # Обработка прочих ошибок
                print(f"Произошла непредвиденная ошибка: {str(e)}")
                print("Пожалуйста, попробуйте снова.")
        note_data = [username, content, description, status, created_date, deadline_date]
        note = dict(zip(heading, note_data))
        notes.append(note)
    else:
        break  # Если ответ не положительный - прерываем цикл
# Выводим список созданных заметок на экран
number = 0
for note_number in notes:
    number = number + 1
    print("Заметка {}: {}".format(number, note_number))
