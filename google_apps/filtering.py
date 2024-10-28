import pandas as pd
df = pd.read_csv('GoogleApps.csv')

# Скільки коштує (Price) найдешевший платний додаток (Type == 'Paid)?
paid = df[df["Type"] == "Paid"]
print(paid["Price"].min())

# Чому дорівнює медіана (median) кількість установок (Installs)
# додатків із категорії (Category) "ART_AND_DESIGN"?
art = df[df["Category"] == "ART_AND_DESIGN"]
print(art["Installs"].median())


# Яка максимальна ціна додатків у категорії BUSINESS?
business = df[df["Category"] == "BUSINESS"]
print(business["Price"].max())

# Яка максимальна кількість відгуків (Reviews) для безкоштовних програм (Type == 'Free')


# Яка максимальна кількість відгуків для платних програм (Type == 'Paid')?

# Який мінімальний розмір (Size) програми для тинейджерів (Content Rating == 'Teen')?


# *До якої категорії (Category) відноситься додаток із найбільшою кількістю відгуків (Reviews)?
max = df[df["Reviews"] == df["Reviews"].max()]
print(max["Category"])

# *Який середній (mean) рейтинг (Rating) додатків вартістю (Price) понад 20 доларів
# із кількістю установок (Installs) більше 10000?
price_installs = df[(df["Price"] > 20) & (df["Installs"] > 10000)]
print(price_installs["Rating"].mean())

# Який максимальний рейтинг додатків, у яких кількість відгуків більше 100 і вони безкоштовні 

