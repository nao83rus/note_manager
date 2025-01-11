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
            if status == '1' or status == 'новая' or status == '2' or status == 'в процессе' or status == '3' or status == 'выполнено':
                break
            else:
                print("Введён неверный статус, попробуйте еще раз.")
        created_date = input('Введите дату создания (день-месяц-год): ')
        deadline_date = input('Введите дедлайн (день-месяц-год): ')
        note_data = [username, content, description, status, created_date, deadline_date]
        note = dict(zip(heading, note_data))
        notes.append(note)
    else:
        break # Если ответ не положительный - прерываем цикл
# Выводим список созданных заметок на экран
for note_number in notes:
    print("Заметка: ", note_number)