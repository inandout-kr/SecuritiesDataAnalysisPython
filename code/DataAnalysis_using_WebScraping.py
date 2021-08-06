import pandas as pd

# 종목코드 불러오는 방법 1 - excel 파일에서
krx_list = pd.read_html('C:/Users/USER/SecuritiesDataAnalysisPython/data/상장법인목록.xls')
krx_list[0].종목코드 = krx_list[0].종목코드.map('{:06d}'.format) # 종목코드 6자리로 변환
print(krx_list[0])

# 종목코드 불러오는 방법 2 - web 파일에서
df = pd.read_html('https://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13')[0]  # 웹 파일에서 불러오기
df['종목코드'] = df['종목코드'].map('{:06d}'.format)
df = df.sort_values(by='종목코드')
df