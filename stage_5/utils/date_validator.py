# Grade 1. Этап 5: Задание 5 Проверяет, соответствует ли дата формату "год-месяц-день".
from datetime import datetime

def validate_date(date_str) -> bool:
    try:
        datetime.strptime(date_str, format('%Y-%m-%d'))
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    # Проверка
    print(f"ГГГГ-ММ-ДД '2025-01-26' {validate_date('2025-01-26')}")
    print(f"ДД-ММ-ГГГГ '25-01-2026' {validate_date('25-01-2026')}")