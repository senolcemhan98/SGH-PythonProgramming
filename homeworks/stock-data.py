#%% DOWNLOAD DATA
import yfinance as yf
keys = ['GOOG','IBM','MSFT']

for key in keys:
    df = yf.download(key, start='2023-01-05', end='2024-01-05')   
    df.to_csv(f'./data/{key}.csv')
#%%

#%%


