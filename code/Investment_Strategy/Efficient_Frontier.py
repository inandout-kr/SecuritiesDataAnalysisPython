import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from AnalyzerFolder import Analyzer


mk = Analyzer.MarketDB()
stock = ['삼성전자', 'SK하이닉스', 'NAVER', '카카오']
df = pd.DataFrame()
for i in stock:
    df[i] = mk.get_daily_price(i, '2018-10-03', '2021-08-28')['close']

daily_ret = df.pct_change()
annual_ret = daily_ret.mean()
daily_cov = daily_ret.cov()
annual_cov = daily_cov * 252

port_ret = []      # 종목 비중 다르게 해 Portfolio 20,000개 생성하기 위한 단계
port_risk = []     # 포트 수익률, 리스크, 비중 저장할 리스트 생성
port_weights = []  #

for _ in range(20000): # 몬테카를로 시뮬레이션 이용해 Portfolio 20,000개 생성
    weights = np.random.random(len(stock))  # stock 개수의 랜덤 숫자로 구성된 배열 생성
    weights /= np.sum(weights)  # 비중의 합이 1이 되도록 조정

    returns = np.dot(weights, annual_ret)  # np.dot 사용해 [(종목별 비중 배열) * (종목별 연간 수익률) = Portfolio 전체 returns] 구하기
    risk = np.sqrt(np.dot(weights.T, np.dot(annual_cov, weights)))  # sqrt((공분산*비중) * 비중의 전치행렬) = Portfolio 전체 Risk 구하기

    port_ret.append(returns) 
    port_risk.append(risk) 
    port_weights.append(weights) 

portfolio = {'Returns': port_ret, 'Risk': port_risk} 
for i, s in enumerate(stock):  # i 값은 0, 1, 2, 3 순으로, s값은 '삼성전자', 'SK하이닉스', 'NAVER', '카카오' 순으로
    portfolio[s] = [weight[i] for weight in port_weights] 
df = pd.DataFrame(portfolio) 
df = df[['Returns', 'Risk'] + [s for s in stock]]
print(portfolio)