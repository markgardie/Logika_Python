import pandas as pd
df = pd.read_csv('GooglePlayStore_wild.csv')

# Очищення даних із першого завдання

# Заміни тип даних на дробове число (float) для цін додатків (Price)
df["Price"] = df["Price"].apply(float)

# Обчисли, скільки доларів розробники заробили на кожному платному додатку
df["Income"] = df["Installs"] * df["Price"]

# Чому дорівнює максимальний дохід ('Profit') серед платних додатків (Type == 'Paid')?


# Створи новий стовпець, у якому зберігатиметься кількість жанрів. Назви його 'Number of genres'

def split_genres(genres):
    return genres.split(";")

df["Genres"] = df["Genres"].apply(split_genres)
df["Number of genres"] = df["Genres"].apply(len)

# Яка максимальна кількість жанрів (Number of genres) зберігається в датасеті?

# Бонусне завдання
# Створи новий стовпець, що зберігає сезон, в якому було зроблено останнє оновлення (Last Updated) програми. Назви його 'Season'

# Виведи на екран сезони та їх кількість у датасеті
