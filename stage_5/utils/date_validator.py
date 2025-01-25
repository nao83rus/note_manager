# Grade 1. Этап 5: Задание 5 Проверяет, соответствует ли дата формату "год-месяц-день".
from datetime import datetime

def validate_date(date_str) -> bool:
    try:
        datetime.strptime(date_str, format('%Y-%m-%d'))
        return True
    except ValueError:
        return False