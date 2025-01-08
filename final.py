heading = ["username", "content", "status", "created_at", "updated_at", "titles"]
note_data = [input("Введите Ваше имя: "), input("Введите содержание заметки: "), input("Введите статус заметки: "),
         input('Введите дату начала в формате \"дата-месяц-год\": '), input('Введите дату изменения в формате \"дата-месяц-год\": ')]
note_titles = [input('Введите заголовок 1: '), input('Введите заголовок 2: ')]
note_data.append(note_titles)
note = dict(zip(heading, note_data))
print(note)