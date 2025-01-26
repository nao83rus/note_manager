# Grade 1. Этап 5: Задание 5 Создаёт уникальный идентификатор для заметки:
import uuid

def generate_unique_id():
    return str(uuid.uuid4())

if __name__ == '__main__':
    # Проверка
    print(str(uuid.uuid4()))