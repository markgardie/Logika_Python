import pandas as pd
df = pd.read_csv(r'google_apps\GoogleApps.csv')

# Скільки коштує (Price) найдешевший платний додаток (Type == 'Paid)?
paid = df[df["Type"] == "Paid"]
min_price = paid["Price"].min()

# Чому дорівнює медіана (median) кількість установок (Installs)
# додатків із категорії (Category) "ART_AND_DESIGN"?
art = df[df["Category"] == "ART_AND_DESIGN"]
installs_media = art["Installs"].median()

#На скільки максимальна кількість відгуків (Reviews) для безкоштовних програм (Type == 'Free')
# більше максимальної кількості відгуків для платних програм (Type == 'Paid')?
paid = df[df["Type"] == "Paid"]
free = df[df["Type"] == "Free"]

paid_reviews = paid["Reviews"].max()
free_reviews = free["Reviews"].max()

print(free_reviews - paid_reviews)
# Який мінімальний розмір (Size) програми для тинейджерів (Content Rating == 'Teen')?
teen = df[df["Content Rating"] == "Teen"]
min_size = teen["Size"].min()

# *До якої категорії (Category) відноситься додаток із найбільшою кількістю відгуків (Reviews)?


# *Який середній (mean) рейтинг (Rating) додатків вартістю (Price) понад 20 доларів
price = df[df["Price"] > 20]
mean_ratin = price["Rating"].mean()
