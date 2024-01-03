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

#Round All Values To Integers
Df = round(Df)

#Isolate data with Index NYA
FinalDf = Df[Df['Index'] == 'NYA']

#Remove Blank Data
DF = FinalDf.dropna()

# Use a Graph to Look for Noise in Dataset
# Relation between Adj Close & Open
plt.figure(figsize=(5,3))
color = "#ff0000"
color_t = "#ff5252"
text_color = "#a70000"
custom_palette = ["#0096c7", "#f72585"]

plt.scatter(DF['Open'],DF['Adj Close'] , color=color)
plt.xticks(rotation=45, ha='right', color=text_color)
plt.yticks(rotation=0, ha='right', color=text_color)
plt.xlabel(' Open ', color=color_t, fontsize=18)
plt.ylabel('Adj Close' , color=color_t, fontsize=18)
plt.grid()
# Show the plot
plt.show()

#Compensate for Noise
OpenAdjCloseNoise1 = DF[(DF['Open'] >= 0) & (DF['Open'] <= 2000) & (DF['Adj Close'] >= 6000) & (DF['Adj Close'] <= 8000)]
DF = DF.drop(OpenAdjCloseNoise1.index)
OpenAdjCloseNoise1 = DF[(DF['Open'] >= 0) & (DF['Open'] <= 2000) & (DF['Adj Close'] >= 6000) & (DF['Adj Close'] <= 8000)]

OpenAdjCloseNoise2 = DF[(DF['Open'] >= 4000) & (DF['Open'] <= 6000) & (DF['Adj Close'] >= 0) & (DF['Adj Close'] <= 2000)]
DF = DF.drop(OpenAdjCloseNoise2.index)
OpenAdjCloseNoise2 = DF[(DF['Open'] >= 4000) & (DF['Open'] <= 6000) & (DF['Adj Close'] >= 0) & (DF['Adj Close'] <= 2000)]

#Plot After Noisy Data Removal
plt.figure(figsize=(5, 3))
color = "#ff0000"
color_t = "#ff5252"
text_color = "#a70000"
custom_palette = ["#0096c7", "#f72585"]

plt.scatter(DF['Open'],DF['Adj Close'] , color=color)
plt.xticks(rotation=45, ha='right', color=text_color)
plt.yticks(rotation=0, ha='right', color=text_color)
plt.xlabel(' Open ', color=color_t, fontsize=18)
plt.ylabel('Adj Close' , color=color_t, fontsize=18)
plt.grid()
# Show the plot
plt.show()

# Use a Graph to Look for Noise in Dataset
# Relation between Adj Close & High
plt.figure(figsize=(5,3))
color = "#ff0000"
color_t = "#ff5252"
text_color = "#a70000"
custom_palette = ["#0096c7", "#f72585"]

plt.scatter(DF['High'],DF['Adj Close'] , color=color)
plt.xticks(rotation=45, ha='right', color=text_color)
plt.yticks(rotation=0, ha='right', color=text_color)
plt.xlabel(' High ', color=color_t, fontsize=18)
plt.ylabel('Adj Close' , color=color_t, fontsize=18)
plt.grid()
# Show the plot
plt.show()

HighAdjCloseNoise = DF[(DF['High'] >= 6000) & (DF['Adj Close'] <= 2500)]
DF = DF.drop(HighAdjCloseNoise.index)
HighAdjCloseNoise = DF[(DF['High'] >= 6000) & (DF['Adj Close'] <= 2500)]

#Plot After Noisy Data Removal
plt.figure(figsize=(5,3))
color = "#ff0000"
color_t = "#ff5252"
text_color = "#a70000"
custom_palette = ["#0096c7", "#f72585"]

plt.scatter(DF['High'],DF['Adj Close'] , color=color)
plt.xticks(rotation=45, ha='right', color=text_color)
plt.yticks(rotation=0, ha='right', color=text_color)
plt.xlabel(' High ', color=color_t, fontsize=18)
plt.ylabel('Adj Close' , color=color_t, fontsize=18)
plt.grid()
# Show the plot
plt.show()

# Use a Graph to Look for Noise in Dataset
# Relation between Adj Close & Low
plt.figure(figsize=(5,3))
color = "#ff0000"
color_t = "#ff5252"
text_color = "#a70000"
custom_palette = ["#0096c7", "#f72585"]

plt.scatter(DF['Low'],DF['Adj Close'] , color=color)
plt.xticks(rotation=45, ha='right', color=text_color)
plt.yticks(rotation=0, ha='right', color=text_color)
plt.xlabel(' Low ', color=color_t, fontsize=18)
plt.ylabel('Adj Close' , color=color_t, fontsize=18)
plt.grid()
# Show the plot
plt.show()

# Use a Graph to Look for Noise in Dataset
# Relation between Adj Close & Close
plt.figure(figsize=(5,3))
color = "#ff0000"
color_t = "#ff5252"
text_color = "#a70000"
custom_palette = ["#0096c7", "#f72585"]

plt.scatter(DF['Close'],DF['Adj Close'] , color=color)
plt.xticks(rotation=45, ha='right', color=text_color)
plt.yticks(rotation=0, ha='right', color=text_color)
plt.xlabel(' Close ', color=color_t, fontsize=18)
plt.ylabel('Adj Close' , color=color_t, fontsize=18)
plt.grid()
# Show the plot
plt.show()

# Create a Heat Map to look for other direct relationships
DF1 = DF[["Open","High","Low", 'Close','Adj Close','Volume']]
plt.figure(figsize=(8, 5))
hm = sns.heatmap(DF1.corr(), annot=True)
# Show the Heat Map
plt.show()

# Plot Adj close over years
plt.figure(figsize=(15, 3))
color = "#f72585"
color_t = "#ff5252"
text_color = "#a70000"
custom_palette = ["#0096c7"]

plt.xticks(rotation=90, ha='right', color=text_color)
plt.yticks(rotation=0, ha='right', color=text_color)
plt.xlabel('year ', color=color_t, fontsize=18)
plt.ylabel('Adj Close' , color=color_t, fontsize=18)
# Show the plot
sns.lineplot(x="year", y="Adj Close", data=DF , color = color)
plt.grid()
# displaying the plot
plt.show()

# Plot Adj close over months with variance shown
plt.figure(figsize=(15, 3))
color = "#f72585"
color_t = "#ff5252"
text_color = "#a70000"
custom_palette = ["#0096c7"]

plt.xticks(rotation=90, ha='right', color=text_color)
plt.yticks(rotation=0, ha='right', color=text_color)
plt.xlabel('month ', color=color_t, fontsize=18)
plt.ylabel('Adj Close' , color=color_t, fontsize=18)
# Show the plot
sns.lineplot(x="month", y="Adj Close", data=DF , color = color)
plt.grid()
# displaying the plot
plt.show()

fig = go.Figure(data=[go.Candlestick(x=DF['year'],
                open=DF['Open'],
                high=DF['High'],
                low=DF['Low'],
                close=DF['Close'])])

fig.show()