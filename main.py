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

df3=df['date'].dt.month
month=[]
for i in df3:
    match i:
        case 1:
            month.append("January")
        case 2:
            month.append("February")
        case 3:
            month.append("March")
        case 4:
            month.append("April")
        case 5:
            month.append("May")
        case 6:
            month.append("June")
        case 7:
            month.append("July")
        case 8:
            month.append("August")
        case 9:
            month.append("September")
        case 10:
            month.append("October")
        case 11:
            month.append("November")
        case 12:
            month.append("December")

df3=pd.DataFrame(month)
df['month'] = df3

#Seperate by month
Df = df[['Index','date','year',"month","Open","High","Low", 'Close','Adj Close','Volume']]
print(Df)