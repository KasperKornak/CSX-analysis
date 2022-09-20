import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

#insert data here
tickers = ['CSX', 'UNP', 'CP', 'CNI', 'NSC','SPY']
start_date = '2012-01-01'
end_date = '2022-08-07'

#data initialization
data = yf.download(tickers, start_date, end_date)
date_format = "%Y-%m-%d"
days = datetime.strptime(end_date, date_format) - datetime.strptime(start_date, date_format)

#calculating total returns
returns = []
i = 0
print('Total returns:')
for ticker in tickers:
    returns.append(data['Adj Close'][ticker][-1] / data['Adj Close'][ticker][0] * 100 - 100)
    print(ticker, ': ', round(returns[i], 2))
    i += 1

#calculating CAGR
cagrs = []
j = 0
print('CAGRs:')
for ticker in tickers:
    cagrs.append(((data['Adj Close'][ticker][-1]/data['Adj Close'][ticker][0]) ** (365/days.days) -1 ) * 100)
    print(ticker, ': ', round(cagrs[j], 2))
    j += 1

#graph
list =[]
sns.set_theme(style='darkgrid', palette='bright')

for ticker in tickers:
    temp = 0
    temp = data['Adj Close'][ticker][1:] / data['Adj Close'][ticker][0] * 100 - 100
    temp.plot(linewidth=1)

plt.xlabel('Years', fontsize = 15)
plt.ylabel('Percent change', fontsize = 15)
plt.title('Performance over 10 year period on adjusted basis', fontsize = 15)
plt.legend(tickers)
plt.xlim([start_date, end_date])
plt.show()
plt.close()