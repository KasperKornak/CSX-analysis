import pandas_datareader as pdr
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns
tickers = ['CSX', 'UNP', 'CP', 'CNI', 'NSC','SPY']
start = dt.datetime(2012, 1, 1)
end = dt.datetime(2022, 8, 7)

data = pdr.get_data_yahoo(tickers, start, end)
data = data['Adj Close']
returns = data / data.shift()

dataplot = sns.heatmap(returns.corr(), cmap="YlGnBu", annot=True)
plt.title('Correlation heatmap')
plt.show()
