# You have access to three files:
#
# #### Bitcoin daily data in US dollars
# - "date" - date from September 17, 2014 to November 17, 2021
# - "open" - the price at the beginning of the trading day
# - "high" - the highest price reached that day
# - "low" - the lowest price reached that day
# - "close" - the price at the closing of the trading day
# - "volume" - how many Bitcoin were traded that day
#
# #### S&P 500 daily data
# - "date" - date from September 17, 2014 to November 17, 2021
# - "open" - the index level at the beginning of the trading day
# - "high" - the highest level reached that day
# - "low" - the lowest level reached that day
# - "close" - the level at the closing of the trading day
# - "volume" - how many shares in the companies that make up the index were traded that day
#
# #### inflation and gold as monthly data
# - "date" - date from September, 2014 to November, 2021
# - "gold_usd" - price in usd of gold for that month
# - "cpi_us" - the inflation index for the US for that month (cpi = consumer price index)
#
# _CPI data from the [U.S. Bureau of Labor Statistics](https://www.bls.gov/cpi/). Publicly available information_.


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
bitcoin = pd.read_csv('./data/bitcoin-usd.csv', parse_dates=['date'])
bitcoin.head()


# In[4]:


sp500 = pd.read_csv('./data/sp500.csv', parse_dates=['date'])
sp500.head()


# In[5]:


monthly_data = pd.read_csv('./data/monthly_data.csv', parse_dates=['date'])
monthly_data.head()

# In[6]:


bitcoin.info()
btc = bitcoin.copy()


# In[7]:


sp = sp500.copy()
sp.info()


# In[8]:


md = monthly_data.copy()
md.info()


# In[9]:


import missingno as msno
msno.matrix(bitcoin)


# In[10]:


is_NaN = btc.isnull()
row_has_NaN = is_NaN.any(axis=1)
rows_with_NaN = btc[row_has_NaN]
print(rows_with_NaN)


# In[11]:


btc.dropna(inplace=True)
btc.info()


# In[12]:


#absolut values plot
plt.figure(figsize = (15,30))
ax1 = plt.subplot(4,1,1)
sns.lineplot(btc['date'], btc['high'],color='Blue')
plt.title('Bitcoin',fontsize=20)
plt.ylabel('Price[USD]',fontsize=15)
plt.xlabel('Date',fontsize=15)
ax2 = plt.subplot(4,1,2)
plt.title('S&P500',fontsize=20)
sns.lineplot(sp['date'], sp['high'],color='black')
plt.ylabel('Price[USD]',fontsize=15)
plt.xlabel('Date',fontsize=15)
ax3 = plt.subplot(4,1,3)
sns.lineplot(md['date'], md['gold_usd'],color='Orange')
plt.title('Gold',fontsize=20)
plt.ylabel('Price[USD]',fontsize=15)
plt.xlabel('Date',fontsize=15)
ax4 = plt.subplot(4,1,4)
sns.lineplot(md['date'], md['cpi_us'],color='Red')
plt.title('CPI in USA',fontsize=20)
plt.ylabel('Value',fontsize=15)
plt.xlabel('Date',fontsize=15)
sns.despine()


# In[13]:


#normalized values
btc['normalized_high'] = btc['high'].div(btc.high.iloc[0]).mul(100)
sp['normalized_high'] = sp['high'].div(sp.high.iloc[0]).mul(100)
md['normalized_gold'] = md['gold_usd'].div(md.gold_usd.iloc[0]).mul(100)
md['normalized_cpi'] = md['cpi_us'].div(md.cpi_us.iloc[0]).mul(100)


# In[14]:


plt.figure(figsize = (15,30))
ax1 = plt.subplot(4,1,1)
sns.lineplot(btc['date'], btc['normalized_high'],color='Blue')
plt.title('Normalized Bitcoin',fontsize=20)
plt.ylabel('Normalized Price',fontsize=15)
plt.xlabel('Date',fontsize=15)
ax2 = plt.subplot(4,1,2)
plt.title('Normalized S&P500',fontsize=20)
sns.lineplot(sp['date'], sp['normalized_high'],color='black')
plt.ylabel('Normalized Price',fontsize=15)
plt.xlabel('Date',fontsize=15)
ax3 = plt.subplot(4,1,3)
sns.lineplot(md['date'], md['normalized_gold'],color='Orange')
plt.title('Normalized Gold',fontsize=20)
plt.ylabel('Normalized Price',fontsize=15)
plt.xlabel('Date',fontsize=15)
ax4 = plt.subplot(4,1,4)
sns.lineplot(md['date'], md['normalized_cpi'],color='Red')
plt.title('Normalized CPI in USA',fontsize=20)
plt.ylabel('Normalized Value',fontsize=15)
plt.xlabel('Date',fontsize=15)
sns.despine()


# In[15]:


#Plot normalized in one graph compared to CPI
plt.figure(figsize = (10,20))
ax1 = plt.subplot(3,1,1)
sns.lineplot(btc['date'], btc['normalized_high'],color='Blue')
sns.lineplot(sp['date'], sp['normalized_high'],color='black')
sns.lineplot(md['date'], md['normalized_gold'],color='Orange')
plt.title('Normalized Asset Values',fontsize=15)
plt.ylabel('Normalized Price, log scale',fontsize=12)
plt.xlabel('Time',fontsize=12)
plt.legend(['Bitcoin','S&P500','Gold'])
ax1.set(yscale = 'log')
#Compare volumes over time
ax1 = plt.subplot(3,1,2)
sns.lineplot(btc['date'], btc['volume'],color='Blue')
sns.lineplot(sp['date'], sp['volume'],color='black')
plt.title('Volumes',fontsize=15)
plt.ylabel('Volume, log scale',fontsize=12)
plt.xlabel('Time',fontsize=12)
ax1.set(yscale = 'log')
plt.legend(['Bitcoin','S&P500'])
ax2 = plt.subplot(3,1,3)
sns.lineplot(md['date'], md['cpi_us'],color='Red')
plt.title('CPI in USA',fontsize=15)
plt.ylabel('CPI Value',fontsize=12)
plt.xlabel('Time',fontsize=12)
sns.despine()


# In[16]:


#Compare volumes over time
plt.figure(figsize = (10,12))
ax1 = plt.subplot(2,1,1)
sns.lineplot(btc['date'], btc['volume'],color='Blue')
sns.lineplot(sp['date'], sp['volume'],color='black')
plt.title('Volumes',fontsize=15)
plt.ylabel('Volume, log scale',fontsize=12)
plt.xlabel('Time',fontsize=12)
ax1.set(yscale = 'log')
plt.legend(['Bitcoin','S&P500'])
ax2 = plt.subplot(2,1,2)
sns.lineplot(md['date'], md['cpi_us'],color='Red')
plt.title('CPI in USA',fontsize=15)
plt.ylabel('CPI Value',fontsize=12)
plt.xlabel('Time',fontsize=12)
sns.despine()


# In[ ]:
