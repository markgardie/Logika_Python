import pandas as pd

df = pd.read_csv('GoogleApps.csv')

# Скільки всього програм з категорією 'BUSINESS'?
print(df["Category"].value_counts())

# Чому рівне співвідношення кількості додатків для підлітків ('Teen') і для дітей старше 10 ('Everyone 10+')?
teen = df[df["Content Rating"] == "Teen"]["App"].count()
everyone_10 = df[df["Content Rating"] == "Everyone 10+"]["App"].count()
print(teen / everyone_10)

# Чому дорівнює середній рейтинг платних програм? Відповідь запиши з точністю до сотих.
print(df[df["Type"] == "Paid"]["Rating"].mean())

# На скільки середній рейтинг безкоштовних додатків менший за середній рейтинг платних?
# free_mean =
# paid_mean = 
# print(paid_mean - free_mean)

# Чому дорівнює мінімальний та максимальний розмір додатків у категорії 'COMICS'?
print(df.groupby("Category")["Size"].agg([min, max]))