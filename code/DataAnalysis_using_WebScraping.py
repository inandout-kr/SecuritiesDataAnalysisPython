import pandas as pd

krx_list = pd.read_html('C:/Users/USER/SecuritiesDataAnalysisPython/data/상장법인목록.xls')
krx_list[0].종목코드 = krx_list[0].종목코드.map('{:06d}'.format) # 종목코드 6자리로 변환
print(krx_list[0])