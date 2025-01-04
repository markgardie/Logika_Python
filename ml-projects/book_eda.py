import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 

df = pd.read_csv("")
  

# Genre
volume_genre = df.loc[:, ["Volume Sales", "Genre"]]

volume_genre_sorted = (
    volume_genre
    .groupby(by = "Genre")
    .sum()
    .sort_values(by="Volume Sales", ascending=False)
    .reset_index()
)

fig, ax = plt.subplots(figsize = (15,15))

ax = sns.barplot(
    data = volume_genre_sorted,
    x = "Volume Sales",
    y= "Genre",
    hue = "Volume Sales",
    palette="flare",
    dodge=False,
)

ax.legend().remove()
plt.show()


