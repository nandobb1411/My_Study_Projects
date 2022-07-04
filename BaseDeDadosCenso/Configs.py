import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_census = pd.read_csv('/home/fernandobellelis/PycharmProjects/pythonProject/BaseDeDadosCenso/Censo.csv')


print(sns.countplot(x = base_census['age']))

# np.unique(base_census['income'], return_counts=True)
