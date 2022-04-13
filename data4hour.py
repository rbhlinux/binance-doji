import pandas as pd
import talib #TA-lib
import numpy as np
import datetime
import os
from binance.client import Client #python-binance
from datetime import datetime, timedelta
import time
#time.sleep(15)


def dateformat(epochxxx):
    epoch = int(epochxxx)/1000
    my_time=datetime.fromtimestamp(epoch).strftime('%d-%b-%y %H:%M')
    return my_time

binance_api="<api>"
binance_secret="<secret>"
client = Client(binance_api,binance_secret)

dt = datetime.today() - timedelta(days=3)
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
df1_newvolume=[]
df1_newopen1=[]
df1_newclose=[]
df1_newlow=[]
df1_newhigh=[]
df1_newdoji=[]
df1_x1 = df1['date']
for i in range(0,leng):
    if int(df1_doji[i]) != 0:
        df1_x2 = dateformat(df1_x1[i])
        df1_newdates.append(df1_x2)

        newvol=round(float(df1_volume[i]),2)
        df1_newvolume.append(newvol)
        newopen1=round(float(df1_open1[i]),2)
        df1_newopen1.append(newopen1)
        newclose=round(float(df1_close[i]),2)
        df1_newclose.append(newclose)
        newlow=round(float(df1_low[i]),2)
        df1_newlow.append(newlow)
        newhigh=round(float(df1_high[i]),2)
        df1_newhigh.append(newhigh)
        newdoji=round(float(df1_doji[i]))
        df1_newdoji.append(newdoji)        

    #BTC ETH NEAR SOL ZIL GMT LUNA WAVES AVAX
fp1=pd.DataFrame({"date":df1_newdates,"open":df1_newopen1,"close":df1_newclose,"high":df1_newhigh,"low":df1_newlow, "volume":df1_newvolume,"DOJI":df1_newdoji})
fp1.loc[len(fp1.index)] = ["BTC","BTC","BTC","BTC","BTC","BTC","BTC"]

df2_date=df2["date"]
df2_open1=df2["open"]
df2_close=df2["close"]
df2_low=df2["low"]
df2_close=df2["close"]
df2_high=df2["high"]
df2_volume=df2["volume"]
df2_doji = talib.CDLDOJI(df2_open1,df2_high, df2_low, df2_close)
df2_newdates = []
df2_newvolume=[]
df2_newopen1=[]
df2_newclose=[]
df2_newlow=[]
df2_newhigh=[]
df2_newdoji=[]
df2_x1 = df2['date']
for i in range(0,leng):
    if int(df2_doji[i]) != 0:
        df2_x2 = dateformat(df2_x1[i])
        df2_newdates.append(df2_x2)

        newvol=round(float(df2_volume[i]),2)
        df2_newvolume.append(newvol)
        newopen1=round(float(df2_open1[i]),2)
        df2_newopen1.append(newopen1)
        newclose=round(float(df2_close[i]),2)
        df2_newclose.append(newclose)
        newlow=round(float(df2_low[i]),2)
        df2_newlow.append(newlow)
        newhigh=round(float(df2_high[i]),2)
        df2_newhigh.append(newhigh)
        newdoji=round(float(df2_doji[i]))
        df2_newdoji.append(newdoji)   
fp2=pd.DataFrame({"date":df2_newdates,"open":df2_newopen1,"close":df2_newclose,"high":df2_newhigh,"low":df2_newlow, "volume":df2_newvolume,"DOJI":df2_newdoji})
fp2.loc[len(fp2.index)] = ["ETH","ETH","ETH","ETH","ETH","ETH","ETH"]

df3_date=df3["date"]
df3_open1=df3["open"]
df3_close=df3["close"]
df3_low=df3["low"]
df3_close=df3["close"]
df3_high=df3["high"]
df3_volume=df3["volume"]
df3_doji = talib.CDLDOJI(df3_open1,df3_high, df3_low, df3_close)

df3_newdates = []
df3_newvolume=[]
df3_newopen1=[]
df3_newclose=[]
df3_newlow=[]
df3_newhigh=[]
df3_newdoji=[]
df3_x1 = df3['date']
for i in range(0,leng):
    if int(df3_doji[i]) != 0:
        df3_x2 = dateformat(df3_x1[i])
        df3_newdates.append(df3_x2)

        newvol=round(float(df3_volume[i]),2)
        df3_newvolume.append(newvol)
        newopen1=round(float(df3_open1[i]),2)
        df3_newopen1.append(newopen1)
        newclose=round(float(df3_close[i]),2)
        df3_newclose.append(newclose)
        newlow=round(float(df3_low[i]),2)
        df3_newlow.append(newlow)
        newhigh=round(float(df3_high[i]),2)
        df3_newhigh.append(newhigh)
        newdoji=round(float(df3_doji[i]))
        df3_newdoji.append(newdoji)        

    #NEAR ETH NEAR SOL ZIL GMT LUNA WAVES AVAX
fp3=pd.DataFrame({"date":df3_newdates,"open":df3_newopen1,"close":df3_newclose,"high":df3_newhigh,"low":df3_newlow, "volume":df3_newvolume,"DOJI":df3_newdoji})
fp3.loc[len(fp3.index)] = ["NEAR","NEAR","NEAR","NEAR","NEAR","NEAR","NEAR"]

df4_date=df4["date"]
df4_open1=df4["open"]
df4_close=df4["close"]
df4_low=df4["low"]
df4_close=df4["close"]
df4_high=df4["high"]
df4_volume=df4["volume"]
df4_doji = talib.CDLDOJI(df4_open1,df4_high, df4_low, df4_close)

df4_newdates = []
df4_newvolume=[]
df4_newopen1=[]
df4_newclose=[]
df4_newlow=[]
df4_newhigh=[]
df4_newdoji=[]
df4_x1 = df4['date']
for i in range(0,leng):
    if int(df4_doji[i]) != 0:
        df4_x2 = dateformat(df4_x1[i])
        df4_newdates.append(df4_x2)

        newvol=round(float(df4_volume[i]),2)
        df4_newvolume.append(newvol)
        newopen1=round(float(df4_open1[i]),2)
        df4_newopen1.append(newopen1)
        newclose=round(float(df4_close[i]),2)
        df4_newclose.append(newclose)
        newlow=round(float(df4_low[i]),2)
        df4_newlow.append(newlow)
        newhigh=round(float(df4_high[i]),2)
        df4_newhigh.append(newhigh)
        newdoji=round(float(df4_doji[i]))
        df4_newdoji.append(newdoji)        

    #SOL ETH SOL SOL ZIL GMT LUNA WAVES AVAX
fp4=pd.DataFrame({"date":df4_newdates,"open":df4_newopen1,"close":df4_newclose,"high":df4_newhigh,"low":df4_newlow, "volume":df4_newvolume,"DOJI":df4_newdoji})
fp4.loc[len(fp4.index)] = ["SOL","SOL","SOL","SOL","SOL","SOL","SOL"]

df5_date=df5["date"]
df5_open1=df5["open"]
df5_close=df5["close"]
df5_low=df5["low"]
df5_close=df5["close"]
df5_high=df5["high"]
df5_volume=df5["volume"]
df5_doji = talib.CDLDOJI(df5_open1,df5_high, df5_low, df5_close)

df5_newdates = []
df5_newvolume=[]
df5_newopen1=[]
df5_newclose=[]
df5_newlow=[]
df5_newhigh=[]
df5_newdoji=[]
df5_x1 = df5['date']
for i in range(0,leng):
    if int(df5_doji[i]) != 0:
        df5_x2 = dateformat(df5_x1[i])
        df5_newdates.append(df5_x2)

        newvol=round(float(df5_volume[i]),2)
        df5_newvolume.append(newvol)
        newopen1=round(float(df5_open1[i]),2)
        df5_newopen1.append(newopen1)
        newclose=round(float(df5_close[i]),2)
        df5_newclose.append(newclose)
        newlow=round(float(df5_low[i]),2)
        df5_newlow.append(newlow)
        newhigh=round(float(df5_high[i]),2)
        df5_newhigh.append(newhigh)
        newdoji=round(float(df5_doji[i]))
        df5_newdoji.append(newdoji)        

    #ZIL ETH ZIL ZIL ZIL GMT LUNA WAVES AVAX
fp5=pd.DataFrame({"date":df5_newdates,"open":df5_newopen1,"close":df5_newclose,"high":df5_newhigh,"low":df5_newlow, "volume":df5_newvolume,"DOJI":df5_newdoji})
fp5.loc[len(fp5.index)] = ["ZIL","ZIL","ZIL","ZIL","ZIL","ZIL","ZIL"]

df6_date=df6["date"]
df6_open1=df6["open"]
df6_close=df6["close"]
df6_low=df6["low"]
df6_close=df6["close"]
df6_high=df6["high"]
df6_volume=df6["volume"]
df6_doji = talib.CDLDOJI(df6_open1,df6_high, df6_low, df6_close)

df6_newdates = []
df6_newvolume=[]
df6_newopen1=[]
df6_newclose=[]
df6_newlow=[]
df6_newhigh=[]
df6_newdoji=[]
df6_x1 = df6['date']
for i in range(0,leng):
    if int(df6_doji[i]) != 0:
        df6_x2 = dateformat(df6_x1[i])
        df6_newdates.append(df6_x2)

        newvol=round(float(df6_volume[i]),2)
        df6_newvolume.append(newvol)
        newopen1=round(float(df6_open1[i]),2)
        df6_newopen1.append(newopen1)
        newclose=round(float(df6_close[i]),2)
        df6_newclose.append(newclose)
        newlow=round(float(df6_low[i]),2)
        df6_newlow.append(newlow)
        newhigh=round(float(df6_high[i]),2)
        df6_newhigh.append(newhigh)
        newdoji=round(float(df6_doji[i]))
        df6_newdoji.append(newdoji)        

    #GMT ETH GMT GMT GMT GMT LUNA WAVES AVAX
fp6=pd.DataFrame({"date":df6_newdates,"open":df6_newopen1,"close":df6_newclose,"high":df6_newhigh,"low":df6_newlow, "volume":df6_newvolume,"DOJI":df6_newdoji})
fp6.loc[len(fp6.index)] = ["GMT","GMT","GMT","GMT","GMT","GMT","GMT"]

df7_date=df7["date"]
df7_open1=df7["open"]
df7_close=df7["close"]
df7_low=df7["low"]
df7_close=df7["close"]
df7_high=df7["high"]
df7_volume=df7["volume"]
df7_doji = talib.CDLDOJI(df7_open1,df7_high, df7_low, df7_close)

df7_newdates = []
df7_newvolume=[]
df7_newopen1=[]
df7_newclose=[]
df7_newlow=[]
df7_newhigh=[]
df7_newdoji=[]
df7_x1 = df7['date']
for i in range(0,leng):
    if int(df7_doji[i]) != 0:
        df7_x2 = dateformat(df7_x1[i])
        df7_newdates.append(df7_x2)

        newvol=round(float(df7_volume[i]),2)
        df7_newvolume.append(newvol)
        newopen1=round(float(df7_open1[i]),2)
        df7_newopen1.append(newopen1)
        newclose=round(float(df7_close[i]),2)
        df7_newclose.append(newclose)
        newlow=round(float(df7_low[i]),2)
        df7_newlow.append(newlow)
        newhigh=round(float(df7_high[i]),2)
        df7_newhigh.append(newhigh)
        newdoji=round(float(df7_doji[i]))
        df7_newdoji.append(newdoji)        

    #LUNA ETH LUNA LUNA LUNA LUNA LUNA WAVES AVAX
fp7=pd.DataFrame({"date":df7_newdates,"open":df7_newopen1,"close":df7_newclose,"high":df7_newhigh,"low":df7_newlow, "volume":df7_newvolume,"DOJI":df7_newdoji})
fp7.loc[len(fp7.index)] = ["LUNA","LUNA","LUNA","LUNA","LUNA","LUNA","LUNA"]

df8_date=df8["date"]
df8_open1=df8["open"]
df8_close=df8["close"]
df8_low=df8["low"]
df8_close=df8["close"]
df8_high=df8["high"]
df8_volume=df8["volume"]
df8_doji = talib.CDLDOJI(df8_open1,df8_high, df8_low, df8_close)

df8_newdates = []
df8_newvolume=[]
df8_newopen1=[]
df8_newclose=[]
df8_newlow=[]
df8_newhigh=[]
df8_newdoji=[]
df8_x1 = df8['date']
for i in range(0,leng):
    if int(df8_doji[i]) != 0:
        df8_x2 = dateformat(df8_x1[i])
        df8_newdates.append(df8_x2)

        newvol=round(float(df8_volume[i]),2)
        df8_newvolume.append(newvol)
        newopen1=round(float(df8_open1[i]),2)
        df8_newopen1.append(newopen1)
        newclose=round(float(df8_close[i]),2)
        df8_newclose.append(newclose)
        newlow=round(float(df8_low[i]),2)
        df8_newlow.append(newlow)
        newhigh=round(float(df8_high[i]),2)
        df8_newhigh.append(newhigh)
        newdoji=round(float(df8_doji[i]))
        df8_newdoji.append(newdoji)        

    #WAVES ETH WAVES WAVES WAVES WAVES WAVES WAVES AVAX
fp8=pd.DataFrame({"date":df8_newdates,"open":df8_newopen1,"close":df8_newclose,"high":df8_newhigh,"low":df8_newlow, "volume":df8_newvolume,"DOJI":df8_newdoji})
fp8.loc[len(fp8.index)] = ["WAVES","WAVES","WAVES","WAVES","WAVES","WAVES","WAVES"]

df9_date=df9["date"]
df9_open1=df9["open"]
df9_close=df9["close"]
df9_low=df9["low"]
df9_close=df9["close"]
df9_high=df9["high"]
df9_volume=df9["volume"]
df9_doji = talib.CDLDOJI(df9_open1,df9_high, df9_low, df9_close)

df9_newdates = []
df9_newvolume=[]
df9_newopen1=[]
df9_newclose=[]
df9_newlow=[]
df9_newhigh=[]
df9_newdoji=[]
df9_x1 = df9['date']
for i in range(0,leng):
    if int(df9_doji[i]) != 0:
        df9_x2 = dateformat(df9_x1[i])
        df9_newdates.append(df9_x2)

        newvol=round(float(df9_volume[i]),2)
        df9_newvolume.append(newvol)
        newopen1=round(float(df9_open1[i]),2)
        df9_newopen1.append(newopen1)
        newclose=round(float(df9_close[i]),2)
        df9_newclose.append(newclose)
        newlow=round(float(df9_low[i]),2)
        df9_newlow.append(newlow)
        newhigh=round(float(df9_high[i]),2)
        df9_newhigh.append(newhigh)
        newdoji=round(float(df9_doji[i]))
        df9_newdoji.append(newdoji)        

    #AVAX ETH AVAX AVAX AVAX AVAX AVAX AVAX AVAX
fp9=pd.DataFrame({"date":df9_newdates,"open":df9_newopen1,"close":df9_newclose,"high":df9_newhigh,"low":df9_newlow, "volume":df9_newvolume,"DOJI":df9_newdoji})
fp9.loc[len(fp9.index)] = ["AVAX","AVAX","AVAX","AVAX","AVAX","AVAX","AVAX"]

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
