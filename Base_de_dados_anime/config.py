import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_anime = pd.read_csv('/home/fernandobellelis/PycharmProjects/pythonProject/Base_de_dados_anime/anime.csv')

fig = px.treemap(base_anime,path=['media_type','nsfw','genres'])
fig.update_traces(root_color="lightgrey")
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()


