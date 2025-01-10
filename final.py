heading = ["username", "content", "status", "created_at", "updated_at", "titles"]
note_data = [input("Введите Ваше имя: "), input("Введите содержание заметки: "), input("Введите статус заметки: "),
         input('Введите дату начала в формате \"дата-месяц-год\": '), input('Введите дату изменения в формате \"дата-месяц-год\": ')]
title1 = input('Введите заголовок заметки 1: ')
title2 = input('Введите заголовок заметки 2: ')
title3 = input('Введите заголовок заметки 3: ')
note_titles = [title1, title2, title3]
note_data.append(note_titles)
note = dict(zip(heading, note_data))
print(note)