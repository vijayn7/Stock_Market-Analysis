import warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

data = pd.read_csv("Market.csv")
df = pd.DataFrame(data)
print(df)