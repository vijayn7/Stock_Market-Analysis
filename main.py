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

#Sort Data By date
df['Date']=pd.to_datetime(df['Date'], utc=True)
df['date'] = [d.date() for d in df['Date']]
correct_date=pd.to_datetime(df['date'], format='%Y-%m-%d').dt.strftime('%m-%d-%Y')
df1=pd.DataFrame(correct_date)
df['date']=df1['date'].astype('datetime64[ns]')
df2=df['date'].dt.year
df['year']=df2.astype('string')
print(df)