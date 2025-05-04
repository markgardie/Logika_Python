import random
import string
from app.models import URL

def generate_short_code(length = 6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def create_short_url(original_url):
    while True:
        short_code = generate_short_code()
        existing_url = URL.get_by_short_code(short_code)
        if not existing_url:
            URL.create(original_url, short_code)
            return short_code