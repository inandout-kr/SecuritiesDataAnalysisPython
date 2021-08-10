import pymysql

connection = pymysql.connect(host='localhost', port=3306, db='dailystockpricedata', 
    user='root', passwd='', autocommit=True)  # connect() 함수 사용해서 connection 객체 생성.

cursor = connection.cursor()  #cursor() 함수 사용해 cursor 객체 생성
cursor.execute("SELECT VERSION();")  #cursor 객체의 execute() 함수를 사용해 SELECT문 실행
result = cursor.fetchone()  # cursor 객체의 fetchone() 함수 사용해 바로 윗줄의 실행 결과를 튜플로 받음

print ("MariaDB version : {}".format(result))

connection.close()