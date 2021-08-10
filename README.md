# SecuritiesDataAnalysisPython
'파이썬 증권 데이터 분석' 책을 이용한 복습


## 1. [주가 데이터 DB 구축](https://github.com/inandout-kr/SecuritiesDataAnalysisPython/tree/main/code/Stock_Price_API/HanStock)
### DBUpdater Class는 매일 한국거래소로부터 상장기업 목록 조회 후, 네이버로부터 일별 시세 읽어와서 MariaDB로 업데이트 함. 매일 오후 5시에 자동 실행(완료).

### MarketDB Class는 야후 파이낸스 API처럼 국내 주식 데이터 조회할 수 있는 함수 제공(개발 진행 중).

---TMI---
(!) DB 구축

* 저자 분 저술 시점에서 야후 파이낸스는 데이터의 정확성이 떨어졌었다. 따라서 보다 정확한 데이터인 네이버 제공 주식 데이터를 사용하고자 하는데, 이는 웹 스크래핑을 통해 가져와야 하기에 느리다.

* 이러한 문제를 해결하기 위해 MariaDB를 이용한 DB 구축.

* (GUI 기반 HeidiSQL로 명령형 인터페이스 기반의 MySQL client보다 편하게 DB 관리)

* (책 저술 시점인 2020.07~2021.01까지는 야후 파이낸스 데이터 이상치 구간 존재했음. 2021.08인 지금 시점에 책 공부하면서 야후 파이낸스 데이터 불러와보니, 책에서 언급한 부분은 결측치 등의 이상한 부분 없었음. 그러나 모든 데이터를 눈으로 확인해보기 쉽지 않으니 일단 책의 내용을 따라 네이버로 가져왔음)


(2) 매일 오후 5시에 DBUpdater 자동 실행 설정


(3) MarketDB Class

* 야후 파이낸스 API처럼 국내 주식 데이터 조회할 수 있는 함수 제공.
* 어떠한 형식으로 날짜 정보(연-월-일) 입력해도 정규표현식을 이용해 숫자가 아닌 하나 이상의 문자(\D+)로 분리하면 날짜 정보(연-월-일)에 해당하는 값을 리스트로 반환 가능함.


*MySQL 명령어
** 데이터베이스 만들기: CREATE DATABASE databaseName;
** DB 목록 확인: SHOW DATABASES;
** 현재 마리아 버전 정보 확인: SELECT VERSION();
** DB 제거: DROP DATABASE databaseName;
