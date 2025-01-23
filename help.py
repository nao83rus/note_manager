notes = [
    {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая'},
    {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе'}]

keyword = input("Введите слово для поиска в полях Имя, Заголовок, Описание: ").lower().strip()
if keyword == '':
    keyword = None

fields_for_search = ["title", "content", "username"]

for note in notes:
    keyword_creteria = True

    # if keyword != None: # сравнение по значение
    if keyword is not None:  # сравнение по ссылки (объект один и тот же)
        for field in fields_for_search:
            # print("keyword: ", keyword, type(keyword))
            # print("value: ", note[field].lower(), type(note[field].lower()))
            # if note[field].lower() == keyword:
            if keyword in note[field].lower().strip():
                print("Найдено")
                keyword_creteria = True
            else:
                print("Не найдено")
                keyword_creteria = False