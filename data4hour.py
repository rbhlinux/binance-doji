import pandas as pd
import talib #TA-lib
import numpy as np
import datetime
import os
from binance.client import Client #python-binance
from datetime import datetime, timedelta


def dateformat(epochxxx):
    epoch = int(epochxxx)/1000
    my_time=datetime.fromtimestamp(epoch).strftime('%d-%b-%y %H:%M')
    return my_time

binance_api="fL2eE0aJzXuHnPocjqL5CLWVz0BYuIoLkhgUZqykOHxfH1uwMFCGXoJLFcsJXv3Y"
binance_secret="iNkQTZLX2IyG1IsIl9W1GoKQgvNmwV7AQqFrXA7X4rxmrFVc3kYsSuIlVGZVZoC9"
client = Client(binance_api,binance_secret)

dt = datetime.today() - timedelta(days=5)
xx1 = dt.replace(hour=00, minute=00,second=00,microsecond=00)
timestamp = int(xx1.timestamp())
timestampthous = timestamp*1000

bars1= client.get_historical_klines('BTCUSDT','4h',timestampthous,limit=500)
bars2= client.get_historical_klines('ETHUSDT','4h',timestampthous,limit=500)
bars3= client.get_historical_klines('NEARUSDT','4h',timestampthous,limit=500)
bars4= client.get_historical_klines('SOLUSDT','4h',timestampthous,limit=500)
bars5= client.get_historical_klines('ZILUSDT','4h',timestampthous,limit=500)
bars6= client.get_historical_klines('GMTUSDT','4h',timestampthous,limit=500)
bars7= client.get_historical_klines('LUNAUSDT','4h',timestampthous,limit=500)
bars8= client.get_historical_klines('WAVESUSDT','4h',timestampthous,limit=500)
bars9= client.get_historical_klines('AVAXUSDT','4h',timestampthous,limit=500)


for line in bars1:
    del line[6:]
for line in bars2:
    del line[6:]
for line in bars3:
    del line[6:]
for line in bars4:
    del line[6:]
for line in bars5:
    del line[6:]
for line in bars6:
    del line[6:]
for line in bars7:
    del line[6:]
for line in bars8:
    del line[6:]
for line in bars9:
    del line[6:]

df1 = pd.DataFrame(bars1, columns=['date', 'open', 'high', 'low', 'close','volume'])
df2 = pd.DataFrame(bars2, columns=['date', 'open', 'high', 'low', 'close','volume'])
df3 = pd.DataFrame(bars3, columns=['date', 'open', 'high', 'low', 'close','volume'])
df4 = pd.DataFrame(bars4, columns=['date', 'open', 'high', 'low', 'close','volume'])
df5 = pd.DataFrame(bars5, columns=['date', 'open', 'high', 'low', 'close','volume'])
df6 = pd.DataFrame(bars6, columns=['date', 'open', 'high', 'low', 'close','volume'])
df7 = pd.DataFrame(bars7, columns=['date', 'open', 'high', 'low', 'close','volume'])
df8 = pd.DataFrame(bars8, columns=['date', 'open', 'high', 'low', 'close','volume'])
df9 = pd.DataFrame(bars9, columns=['date', 'open', 'high', 'low', 'close','volume'])
leng=len(df1["date"])

df1_date=df1["date"]
df1_open1=df1["open"]
df1_close=df1["close"]
df1_low=df1["low"]
df1_close=df1["close"]
df1_high=df1["high"]
df1_volume=df1["volume"]
df1_doji = talib.CDLDOJI(df1_open1,df1_high, df1_low, df1_close)
df1_newdates = []
df1_x1 = df1['date']
for i in range(0,leng):
    df1_x2 = dateformat(df1_x1[i])
    df1_newdates.append(df1_x2)
fp1=pd.DataFrame({"date":df1_newdates,"open":df1_open1,"close":df1_close,"high":df1_high,"low":df1_low, "volume":df1_volume,"DOJI":df1_doji})

df2_date=df2["date"]
df2_open1=df2["open"]
df2_close=df2["close"]
df2_low=df2["low"]
df2_close=df2["close"]
df2_high=df2["high"]
df2_volume=df2["volume"]
df2_doji = talib.CDLDOJI(df2_open1,df2_high, df2_low, df2_close)
df2_newdates = []
df2_x1 = df2['date']
for i in range(0,leng):
    df2_x2 = dateformat(df2_x1[i])
    df2_newdates.append(df2_x2)
fp2=pd.DataFrame({"date":df2_newdates,"open":df2_open1,"close":df2_close,"high":df2_high,"low":df2_low, "volume":df2_volume,"DOJI":df2_doji})

df3_date=df3["date"]
df3_open1=df3["open"]
df3_close=df3["close"]
df3_low=df3["low"]
df3_close=df3["close"]
df3_high=df3["high"]
df3_volume=df3["volume"]
df3_doji = talib.CDLDOJI(df3_open1,df3_high, df3_low, df3_close)
df3_newdates = []
df3_x1 = df3['date']
for i in range(0,leng):
    df3_x2 = dateformat(df3_x1[i])
    df3_newdates.append(df3_x2)
fp3=pd.DataFrame({"date":df3_newdates,"open":df3_open1,"close":df3_close,"high":df3_high,"low":df3_low, "volume":df3_volume,"DOJI":df3_doji})

df4_date=df4["date"]
df4_open1=df4["open"]
df4_close=df4["close"]
df4_low=df4["low"]
df4_close=df4["close"]
df4_high=df4["high"]
df4_volume=df4["volume"]
df4_doji = talib.CDLDOJI(df4_open1,df4_high, df4_low, df4_close)
df4_newdates = []
df4_x1 = df4['date']
for i in range(0,leng):
    df4_x2 = dateformat(df4_x1[i])
    df4_newdates.append(df4_x2)
fp4=pd.DataFrame({"date":df4_newdates,"open":df4_open1,"close":df4_close,"high":df4_high,"low":df4_low, "volume":df4_volume,"DOJI":df4_doji})

df5_date=df5["date"]
df5_open1=df5["open"]
df5_close=df5["close"]
df5_low=df5["low"]
df5_close=df5["close"]
df5_high=df5["high"]
df5_volume=df5["volume"]
df5_doji = talib.CDLDOJI(df5_open1,df5_high, df5_low, df5_close)
df5_newdates = []
df5_x1 = df5['date']
for i in range(0,leng):
    df5_x2 = dateformat(df5_x1[i])
    df5_newdates.append(df5_x2)
fp5=pd.DataFrame({"date":df5_newdates,"open":df5_open1,"close":df5_close,"high":df5_high,"low":df5_low, "volume":df5_volume,"DOJI":df5_doji})

df6_date=df6["date"]
df6_open1=df6["open"]
df6_close=df6["close"]
df6_low=df6["low"]
df6_close=df6["close"]
df6_high=df6["high"]
df6_volume=df6["volume"]
df6_doji = talib.CDLDOJI(df6_open1,df6_high, df6_low, df6_close)
df6_newdates = []
df6_x1 = df6['date']
for i in range(0,leng):
    df6_x2 = dateformat(df6_x1[i])
    df6_newdates.append(df6_x2)
fp6=pd.DataFrame({"date":df6_newdates,"open":df6_open1,"close":df6_close,"high":df6_high,"low":df6_low, "volume":df6_volume,"DOJI":df6_doji})

df7_date=df7["date"]
df7_open1=df7["open"]
df7_close=df7["close"]
df7_low=df7["low"]
df7_close=df7["close"]
df7_high=df7["high"]
df7_volume=df7["volume"]
df7_doji = talib.CDLDOJI(df7_open1,df7_high, df7_low, df7_close)
df7_newdates = []
df7_x1 = df7['date']
for i in range(0,leng):
    df7_x2 = dateformat(df7_x1[i])
    df7_newdates.append(df7_x2)
fp7=pd.DataFrame({"date":df7_newdates,"open":df7_open1,"close":df7_close,"high":df7_high,"low":df7_low, "volume":df7_volume,"DOJI":df7_doji})

df8_date=df8["date"]
df8_open1=df8["open"]
df8_close=df8["close"]
df8_low=df8["low"]
df8_close=df8["close"]
df8_high=df8["high"]
df8_volume=df8["volume"]
df8_doji = talib.CDLDOJI(df8_open1,df8_high, df8_low, df8_close)
df8_newdates = []
df8_x1 = df8['date']
for i in range(0,leng):
    df8_x2 = dateformat(df8_x1[i])
    df8_newdates.append(df8_x2)
fp8=pd.DataFrame({"date":df8_newdates,"open":df8_open1,"close":df8_close,"high":df8_high,"low":df8_low, "volume":df8_volume,"DOJI":df8_doji})

df9_date=df9["date"]
df9_open1=df9["open"]
df9_close=df9["close"]
df9_low=df9["low"]
df9_close=df9["close"]
df9_high=df9["high"]
df9_volume=df9["volume"]
df9_doji = talib.CDLDOJI(df9_open1,df9_high, df9_low, df9_close)
df9_newdates = []
df9_x1 = df9['date']
for i in range(0,leng):
    df9_x2 = dateformat(df9_x1[i])
    df9_newdates.append(df9_x2)
fp9=pd.DataFrame({"date":df9_newdates,"open":df9_open1,"close":df9_close,"high":df9_high,"low":df9_low, "volume":df9_volume,"DOJI":df9_doji})


#BTC ETH NEAR SOL ZIL GMT LUNA WAVES AVAX

path = "/home/code/4hour/"
fp1.to_csv(str(path)+str("BTC.csv"))
fp2.to_csv(str(path)+str("ETH.csv"))
fp3.to_csv(str(path)+str("NEAR.csv"))
fp4.to_csv(str(path)+str("SOL.csv"))
fp5.to_csv(str(path)+str("ZIL.csv"))
fp6.to_csv(str(path)+str("GMT.csv"))
fp7.to_csv(str(path)+str("LUNA.csv"))
fp8.to_csv(str(path)+str("WAVES.csv"))
fp9.to_csv(str(path)+str("AVAX.csv"))

