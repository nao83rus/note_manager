heading = ["username", "content", "status", "created_at", "updated_at", "titles"]
note1 = [input("Введите Ваше имя: "), input("Введите содержание заметки: "), input("Введите статус заметки: "),
         input('Введите дату начала в формате \"дата-месяц-год\": '), input('Введите дату изменения в формате \"дата-месяц-год\": ')]
note1_1 = [input('Введите заголовок 1: '), input('Введите заголовок 2: ')]
note1.append(note1_1)
note = dict(zip(heading, note1))
print(note)