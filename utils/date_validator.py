from datetime import datetime

# проверим что дата дедлайна в валидном формате
def validate_date(date_str) -> bool:
    try:
        datetime.strptime(date_str, format('%Y-%m-%d'))
        return True
    except ValueError:
        return False