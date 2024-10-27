import pandas as pd
df = pd.read_csv(r'google_apps\GoogleApps.csv')

# 1 Скільки всього програм з категорією ('Category') 'BUSINESS'?
print(df['Category'].value_counts())

# 2 Чому дорівнює співвідношення кількості додатків для підлітків ('Teen') і для дітей старше 10 ('Everyone 10+')?
# Відповідь запиши з точністю до сотих.
age_groups = df["Content Rating"].value_counts()
ratio = age_groups["Teen"] / age_groups["Everyone 10+"]
print(round(ratio, 2))

# 3.1 Чому дорівнює середній рейтинг ('Rating') платних ('Paid') додатків?
# Відповідь запиши з точністю до сотих.
app_type = df.groupby(by = "Type")
mean_rating = app_type["Rating"].mean()
print(round(mean_rating["Paid"], 2))

# 3.2 На скільки середній рейтинг ('Rating') безкоштовних ('Free') додатків менший за середній рейтинг платних ('Paid')?
# Відповідь запиши з точністю до сотих.
print(round(mean_rating["Paid"] - mean_rating["Free"], 2))

# 4 Чому дорівнює мінімальний та максимальний розмір ('Size') додатків у категорії ('Category') 'COMICS'?
# Запиши відповіді з точністю до сотих.
categories = df.groupby(by = "Category")
min_size = categories["Size"].min()
max_size = categories["Size"].max()
print(round(min_size["COMICS"], 2))
print(round(max_size["COMICS"], 2))

group = df["Category"].value_counts()
print(group["ART_AND_DESIGN"])

# Бонус 1. Скільки додатків з рейтингом ('Rating') більше 4.5 у категорії ('Category') 'FINANCE'?



# Бонус 2. Чому дорівнює співвідношення безкоштовних ('Free') і платних ('Paid') ігор з рейтингом ('Rating') більше 4.9?

