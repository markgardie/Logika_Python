import pandas as pd

df = pd.read_csv(r'google_apps\GoogleApps.csv')

print(df.info())

print(df.describe())

print(df.head())

print(df.tail())