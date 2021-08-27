import numpy as numpy
import pandas as pd
import matplotlib.pylab as plt
from AnalyzerFolder import Analyzer


mk = Analyzer.MarketDB()
stock = ['삼성전자', 'SK하이닉스', '현대자동차', 'NAVER']
df = pd.DataFrame()
for i in stock:
    df[i] = mk.get_daily_price(i, '2018-10-03', '2021-08-28')['close']

daily_ret = df.pct_change()
annual_ret = daily_ret.mean()
daily_cov = daily_ret.cov()
annual_cov = daily_cov * 252

print(annual_ret)
print(annual_cov)
