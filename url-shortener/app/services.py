import random
import string
from app.models import URL

def generate_short_code(length=6):
    """Генерує випадковий короткий код заданої довжини"""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def create_short_url(original_url):
    """Створює короткий URL, перевіряючи на унікальність"""
    while True:
        short_code = generate_short_code()
        # Перевіряємо, чи код вже використовується
        existing_url = URL.get_by_short_code(short_code)
        if not existing_url:
            # Якщо код унікальний, створюємо запис
            URL.create(original_url, short_code)
            return short_code