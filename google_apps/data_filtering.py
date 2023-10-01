import pandas as pd
df = pd.read_csv('google_apps\GoogleApps.csv')


# Скільки коштує (Price) найдешевший платний додаток (Type == 'Paid)?
print(df[df["Type"] == "Paid"]["Price"].min())

# Чому дорівнює медіанна (median) кількість установок (Installs)
# додатків із категорії (Category) "ART_AND_DESIGN"?
print(df[df["Category"] == "ART_AND_DESIGN"]["Installs"].median())

# На скільки максимальна кількість відгуків (Reviews) для безкоштовних програм (Type == 'Free')
# більше максимальної кількості відгуків для платних програм (Type == 'Paid')?
free = df[df["Type"] == "Free"]["Reviews"].max()
paid = df[df["Type"] == "Paid"]["Reviews"].max()

print(free - paid)

# Який мінімальний розмір (Size) програми для тинейджерів (Content Rating == 'Teen')?
teen = df[df["Content Rating"] == "Teen"]["Size"].min()
print(teen)

# *До якої категорії (Category) відноситься додаток із найбільшою кількістю відгуків (Reviews)?
reviews = df[df["Reviews"] == df["Reviews"].max()]["Category"]
print(reviews)

# *Який середній (mean) рейтинг (Rating) додатків вартістю (Price) понад 20 доларів
# з кількістю установок (Installs) понад 10000?
res = df[(df["Price"] > 20) & (df["Installs"] > 10000)]["Rating"].mean()
print(res)