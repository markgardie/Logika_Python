import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from plotly import express as px
import cufflinks as cf
import plotly.graph_objects as go

url = ''
df = pd.read_csv(url)

corr=df.corr()
plt.figure(figsize=(15,10))
sns.heatmap(corr,annot=True)

df_years = df.groupby(by = "year", as_index = False)
px.line(
    df_years, 
    x = "year", 
    y = "Profit", 
    labels = {"x": "Year", "y": "Profit"},
    title = "Gross By Years"
)

fig = go.Figure()
fig.add_trace(go.Scatter(x=year_cat.year,y=year_cat['Product Category_Accessories'],mode='lines',name='Accessories'))
fig.add_trace(go.Scatter(x=year_cat.year,y=year_cat['Product Category_Bikes'],mode='lines',name='Bikes'))
fig.add_trace(go.Scatter(x=year_cat.year,y=year_cat['Product Category_Clothing'],mode='lines',name='Clothing'))