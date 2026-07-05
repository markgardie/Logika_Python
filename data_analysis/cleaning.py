import pandas as pd

# Зчитування датасету
df = pd.read_csv('googleplaystore.csv')

df.info()

# --- Попереднє очищення ---
# Видалення рядка з помилковими даними (наприклад, де Price = 'Everyone' або Installs = 'Free'),
# оскільки це заважає подальшій конвертації типів.
df = df[df["Price"] != "Everyone"]

# --- 1. Нормалізація поля Rating ---
# Заміна NaN на середній рейтинг по колонці
df["Rating"] = df["Rating"].fillna(df["Rating"].mean()) 

# --- 2. Нормалізація поля Size ---
# Заміна 'Varies with device' на -1
df["Size"] = df["Size"].replace("Varies with device", -1)

# Функція для конвертації розмірів
def convert_size(size_str):
    if str(size_str) == "-1":
        return -1.0
    if "M" in str(size_str):
        return float(str(size_str).replace("M", ""))
    if "k" in str(size_str):
        return float(str(size_str).replace("k", "")) / 1024
    
    return float(size_str)

# Застосування функції
df["Size"] = df["Size"].apply(convert_size)

# --- 3. Нормалізація поля Installs ---
# Видалення '+' та ',', перетворення на int
# Використовуємо regex=False для безпечної заміни спецсимволів
df["Installs"] = df["Installs"].str.replace("+", "", regex = False).str.replace(",", "", regex=False)
df["Installs"] = df["Installs"].astype(int)


# --- 4. Нормалізація поля Type ---
# Заміна пропусків на 'Free'


# --- 5. Нормалізація поля Price ---
# Видалення '$', перетворення на float


# Перевірка результату
