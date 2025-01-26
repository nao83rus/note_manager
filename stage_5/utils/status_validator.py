# Grade 1. Этап 5: Задание 5 Проверяет, что статус является допустимым.
def validate_status(status):
    if status.lower() in ['новая', 'в процессе', 'отложена', 'завершена']:
        return True
    else:
        return False