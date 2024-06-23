import pandas as pd
df = pd.read_csv(r"D:\Mark\Desktop\Logika_Python\google_apps\GoogleApps.csv")


# 1 Скільки всього програм з категорією ('Category') 'BUSINESS'?
print(df["Category"].value_counts())


# 2 Чому дорівнює співвідношення кількості додатків для підлітків ('Teen') і для дітей старше 10 ('Everyone 10+')?
# Відповідь запиши з точністю до сотих.
temp = df["Content Rating"].value_counts()
result = temp["Teen"] / temp["Everyone 10+"]
result = round(result, 2)
print(result)



# 3.1 Чому дорівнює середній рейтинг ('Rating') платних ('Paid') додатків?
# Відповідь запиши з точністю до сотих.
temp = df.groupby(by = "Type")
rating_mean = temp["Rating"].mean()
print(round(rating_mean["Paid"], 2))


# 3.2 На скільки середній рейтинг ('Rating') безкоштовних ('Free') додатків менший за середній рейтинг платних ('Paid')?
# Відповідь запиши з точністю до сотих.
print(round(rating_mean["Free"] - rating_mean["Paid"], 2))


# 4 Чому дорівнює мінімальний та максимальний розмір ('Size') додатків у категорії ('Category') 'COMICS'?
# Запиши відповіді з точністю до сотих.
temp = df.groupby(by = "Category")
size_min = temp["Size"].min()
size_max = temp["Size"].max()
print(round(size_min["COMICS"], 2))
print(round(size_max["COMICS"], 2))

# Бонус 1. Скільки додатків з рейтингом ('Rating') більше 4.5 у категорії ('Category') 'FINANCE'?
filt = df[df["Rating"] > 4.5]
group = filt["Category"].value_counts()
print(group["FINANCE"])


# Бонус 2. Чому дорівнює співвідношення безкоштовних ('Free') і платних ('Paid') ігор з рейтингом ('Rating') більше 4.9?

