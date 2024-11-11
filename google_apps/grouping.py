import pandas as pd
df = pd.read_csv(r"google_apps\GoogleApps.csv")


# 1 Скільки всього програм з категорією ('Category') 'BUSINESS'?
business_count = df["Category"].value_counts()
print(business_count["BUSINESS"])

# 1.2 Скільки додатків створено для підлітків (Content Rating, Teen)


# 2 Чому дорівнює співвідношення кількості додатків для підлітків ('Teen') і для дітей старше 10 ('Everyone 10+')?
# Відповідь запиши з точністю до сотих. 
temp = df["Content Rating"].value_counts()
temp = temp["Teen"] / temp["Everyone 10+"]
print(temp)

# 2.1 На скільки кількість безкоштовних додатків більша за кількість платних додатків. 
temp = df["Type"].value_counts()
temp = temp["Free"] - temp["Paid"]
print(temp)


# 3.1 Чому дорівнює середній рейтинг ('Rating') платних ('Paid') додатків?
# Відповідь запиши з точністю до сотих.
temp = df.groupby(by = "Type")
temp = temp["Rating"].mean()
print(round(temp["Paid"], 2))

# 3.2 Чому дорівнює середня ціна додатків в категорії BUSINESS
# Відповідь запиши з точністю до сотих.
temp = df.groupby(by = "Category")
temp = temp["Price"].mean()
print(round(temp["BUSINESS"], 2))

# 3.3 Чому дорівнює мінімальна ціна в категорії EDUCATION?
temp = df.groupby(by = "Category")
temp = temp["Price"].mean()
print(round(temp["BUSINESS"], 2))

# dz 1.1. Скільки додатків в категорії SOCIAL

# dz 1.2 Скільки додатків в групі Everyone

# dz 2.1 Чому дорівнює максимальний рейтинг в групі Teen?

# dz 2.2 Чому дорівнює середня кількість установок в категорії MEDICAL



# 4 Чому дорівнює мінімальний та максимальний розмір ('Size') додатків у категорії ('Category') 'COMICS'?
# Запиши відповіді з точністю до сотих.

# Бонус 1. Скільки додатків з рейтингом ('Rating') більше 4.5 у категорії ('Category') 'FINANCE'?



# Бонус 2. Чому дорівнює співвідношення безкоштовних ('Free') і платних ('Paid') ігор з рейтингом ('Rating') більше 4.9?