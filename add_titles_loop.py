# add_titles_loop.py Grade 1. Этап 2: Задание 1 Цикл для добавления заголовков
# создадим пустой список заголовков
note_titles = []
#Реализуем возможность ввода неограниченного числа заголовков используя бесконечный цикл
while True:
    title_ = input('Введите заголовок (или оставьте пустым для завершения): ')
    #Проверяем не пустой ли заголовок
    if title_ == '':
        #Введено пустое значение, прерываем цикл
        break
    #Введено не пустое значение, проверяем его на уникальность и добавляем его в список заголовков, если он уникальный
    for title in note_titles:
        if title.count(title_) >= 1:
            print("Такой заголовок уже есть.")
            break
    else:
        print("Все заголовки уникальны.")
        note_titles.append(title_)
#Цикл окончен. Выводим список заголовков
print("Ввод данных закончен. Список заголовков:")
counter = 0
for note in note_titles:
    print(f"Заголовок №{note}: {note_titles[counter]}")
    counter = counter + 1
