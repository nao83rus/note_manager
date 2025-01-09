# Импортируем необходимые модули для работы с датами
from datetime import datetime
today = datetime.today()
print('Текущая дата: ', today)

# Основной блок программы
while True:
    try:
        # Запрашиваем дату дедлайна у пользователя
        issue_date = input("Введите дату дедлайна (в формате день-месяц-год, например 31-01-2025): ")

        # Преобразуем строку с датой в объект datetime
        deadline_date = datetime.strptime(issue_date, "%d-%m-%Y")
        # Вычисляем разницу между текущей датой и дедлайном. Учитываем только дату без времени.
        time_difference = deadline_date.date() - today.date()
        days_difference = time_difference.days
        # Проверяем статус дедлайна и выводим соответствующее сообщение
        if days_difference < 0:
            # abs() убирает минус в строке вывода и выводит абсолютное значение
            print(f"Внимание! Дедлайн истёк {abs(days_difference)} д. назад.")
        elif days_difference == 0:
            print("Дедлайн сегодня!")
        else:
            print(f"До дедлайна осталось {days_difference} д.")

        # Прерываем цикл после успешной обработки даты
        break

    except ValueError:
        # Обработка ошибки неверного формата даты
        print("Ошибка! Пожалуйста, введите дату в правильном формате (день-месяц-год).")
        print("Пример: 31-01-2025")

    except Exception as e:
        # Обработка прочих ошибок
        print(f"Произошла непредвиденная ошибка: {str(e)}")
        print("Пожалуйста, попробуйте снова.")