notes = [
    {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю',
     'status': 'новая', 'created_date': '2025-1-10', 'issue_date': '2025-1-30'},
    {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену',
     'status': 'в процессе', 'created_date': '2025-2-10', 'issue_date': '2025-2-20'},
    {'username': 'Игорь', 'title': 'Спорт', 'content': 'Подготовиться к соревнованиям',
     'status': 'в процессе', 'created_date': '2025-2-10', 'issue_date': '2025-2-20'},
]

keyword = input("Введите слово для поиска в полях Имя, Заголовок, Описание: ").lower().strip()
if keyword == '':
    keyword = None

fields_for_search = ["title", "content", "username"]

for note in notes:
    keyword_creteria = True

    # if keyword != None: # сравнение по значение
    if keyword is not None:  # сравнение по ссылки (объект один и тот же)
        for field in fields_for_search:
            if keyword in note[field].lower().strip():
                print("Найдено")
                keyword_creteria = True
            else:
                print("Не найдено")
                keyword_creteria = False