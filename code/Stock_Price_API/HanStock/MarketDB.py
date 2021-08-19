import pandas as pd
#from bs4 import BeautifulSoup
#import urllib
#from urllib.request import urlopen
import pymysql
#import time
#import pandas.io.sql as sql
from datetime import datetime
#from threading import Timer
#import matplotlib.pyplot as plt

class MarketDB:
    def __init__(self):
        """생성자: MariaDB 연결 및 종목코드 딕셔너리 생성"""
        self.conn = pymysql.connect(host='localhost', user='root', password='rldnd1684!', db='dailystockpricedata', charset='utf8')  #인스턴스 멤버인 conn 객체 생성
        self.codes = dict()  # 리터럴 사용해 딕셔너리 생성
        self.getCompanyInfo()  # 함수 호출해 마리아DB에서 company_info 테이블 읽어와 codes에 저장
        
    def __del__(self):
        """소멸자: MariaDB 연결 해제"""
        self.conn.close()

    def getCompanyInfo(self):
        """company_info 테이블에서 읽어와서 companyData와 codes에 저장"""
        sql = "SELECT * FROM company_info"
        companyInfo = pd.read_sql(sql, self.conn)
        for idx in range(len(companyInfo)):
            self.codes[companyInfo['code'].values[idx]] = companyInfo['company'].values[idx]

    def getDailyPrice(self, code, startDate, endDate):
        """daily_price 테이블에서 KRX 종목 시세 읽어와서 데이터프레임으로 반환"""
        sql = "SELECT * FROM daily_price WHERE code = '{}' and date >= '{}' and date <= '{}'".format(code, startDate, endDate)
        df = pd.read_sql(sql, self.conn)
        df.index = df['date']
        return df



