import pandas as pd
df = pd.read_csv('GoogleApps.csv')


# Скільки коштує (Price) найдешевший платний додаток (Type == 'Paid)?
paid = df[df["Type"] == "Paid"]
min = paid["Price"].min()
print(min)

# Чому дорівнює медіана (median) кількість установок (Installs)
# додатків із категорії (Category) "ART_AND_DESIGN"?
art = df[df["Category"] == "ART_AND_DESIGN"]
med_inst = art["Installs"].median()
print(med_inst)

#На скільки максимальна кількість відгуків (Reviews) для безкоштовних програм (Type == 'Free')
# більше максимальної кількості відгуків для платних програм (Type == 'Paid')?
free = df[df["Type"] == "Free"]
paid = df[df["Type"] == "Paid"]
free_max = free["Reviews"].max()
paid_max = paid["Reviews"].max()
print(free_max - paid_max)

# Який мінімальний розмір (Size) програми для тинейджерів (Content Rating == 'Teen')?



# *До якої категорії (Category) відноситься додаток із найбільшою кількістю відгуків (Reviews)?



# *Який середній (mean) рейтинг (Rating) додатків вартістю (Price) понад 20 доларів
# із кількістю установок (Installs) більше 10000?

filt = df[(df["Installs"] > 10000) & (df["Price"] > 20)]


# додатково
df[df["Installs"] > 10000]
