import pandas as pd

df = pd.read_csv("google_apps\GoogleApps.csv")

print(df.info())
print(df.describe())
print(df.head(5))
print(df.tail(5))

