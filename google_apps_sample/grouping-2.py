import pandas as pd
df = pd.read_csv('GoogleApps.csv')

# 1 Виведи на екран мінімальний, середній та максимальний рейтинг ('Rating') платних та безкоштовних програм ('Type') з точністю до десятих.
print(round(df.groupby(by = 'Type')['Rating'].agg(['min', 'mean', 'max']), 1))

# 2 Виведи на екран мінімальну, медіанну (median) та максимальну ціну ('Price') платних додатків (Type == 'Paid') для
# різних цільових аудиторій ('Content Rating')
print(df[df['Type'] == 'Paid'].groupby(by = 'Content Rating')['Price'].agg(['min', 'median', 'max']))

# 3 Згрупуй дані за категорією ('Category') та цільовою аудиторією ('Content Rating') будь-яким зручним для тебе способом
# Порахуй максимальну кількість відгуків ('Reviews') у кожній групі.
# Порівняй результати для категорій 'EDUCATION', 'FAMILY' та 'GAME':
# У якій віковій групі найбільше відгуків отримала програма з категорії 'EDUCATION'? 'FAMILY'? 'GAME'?
# Підказка: ти можеш вибрати з DataFrame кілька стовпців одночасно за допомогою такого синтаксису:
# df [[<стовпець 1>, <стовпець 2>, <стовпець 3>]]
temp = df.pivot_table(index = 'Content Rating', columns = 'Category', values = 'Reviews', aggfunc = 'max')
print(temp[['EDUCATION', 'FAMILY', 'GAME']])

# 4 Згрупуй платні (Type == 'Paid') програми за категорією ('Category') та цільовою аудиторією ('Content Rating')
# Порахуй середню кількість відгуків ('Reviews') у кожній групі
# Зверніть увагу, що в деяких клітинках отриманої таблиці відображається не число, а значення "NaN" - Not a Number
# Цей запис означає, що в цій групі немає жодної програми.
# Вибери назви категорій, в яких є платні програми для всіх вікових груп і розташуй їх в алфавітному порядку.
print(df[df['Type'] == 'Paid'].pivot_table(columns = 'Content Rating', index = 'Category', values = 'Reviews', aggfunc = 'mean'))

# Бонусне завдання. Знайди категорії безкоштовних (Type == 'Free') додатків,
# у яких програми розроблені не для всіх вікових груп ('Content Rating')
