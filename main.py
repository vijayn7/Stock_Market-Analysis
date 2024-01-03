import warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

data = pd.read_csv("Market.csv")
df = pd.DataFrame(data)
info = df.info()
describe = df.describe()

print(df)

#Sort Data By date
df['Date']=pd.to_datetime(df['Date'], utc=True)
df['date'] = [d.date() for d in df['Date']]
print(df)