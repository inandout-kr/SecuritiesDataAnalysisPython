# SecuritiesDataAnalysisPython
'파이썬 증권 데이터 분석' 책을 이용한 복습

*현재 DB 내 2021-08-05 기간 이후 데이터에 이상치 이슈 발생. 해결 중


## 1. [주가 데이터 DB 구축](https://github.com/inandout-kr/SecuritiesDataAnalysisPython/tree/main/code/Stock_Price_API/HanStock)

국내 유가증권시장, 코스닥 내 전 종목의 일별 종가 DB를 구축해서, 필요할 때마다 간편하게 데이터를 사용할 수 있도록 구축함.

추후 틱 데이터도 모을 예정임.

#### DBUpdater Class는 매일 한국거래소로부터 상장기업 목록 조회 후, 네이버로부터 일별 시세 읽어와서 MariaDB로 업데이트 함. 매일 오후 5시에 자동 실행(완료).

#### MarketDB Class는 야후 파이낸스 API처럼 국내 주식 데이터 조회할 수 있는 함수 제공(완료).



(1) DB 구축
  * 저자 분 저술 시점에서 야후 파이낸스는 데이터의 정확성이 떨어졌었다. 따라서 보다 정확한 데이터인 네이버 제공 주식 데이터를 사용하고자 하는데, 이는 웹 스크래핑을 통해 가져와야 하기에 느리다.
  * 이러한 문제를 해결하기 위해 MariaDB를 이용한 DB 구축.
  * (GUI 기반 HeidiSQL로 명령형 인터페이스 기반의 MySQL client보다 편하게 DB 관리)
  * (책 저술 시점인 2020.07~2021.01까지는 야후 파이낸스 데이터 이상치 구간 존재했음. 2021.08인 지금 시점에 책 공부하면서 야후 파이낸스 데이터 불러와보니, 책에서 언급한 부분은 결측치 등의 이상한 부분 없었음. 그러나 모든 데이터를 눈으로 확인해보기 쉽지 않으니 일단 책의 내용을 따라 네이버로 가져왔음)


(2) 매일 오후 5시에 DBUpdater 자동 실행 설정


(3) MarketDB Class
 * 야후 파이낸스 API처럼 국내 주식 데이터 조회할 수 있는 함수 제공.
 * 어떠한 형식으로 날짜 정보(연-월-일) 입력해도 정규표현식을 이용해 숫자가 아닌 하나 이상의 문자(\D+)로 분리하면 날짜 정보(연-월-일)에 해당하는 값을 리스트로 반환 가능함.



## 2. [투자 전략 구현](https://github.com/inandout-kr/SecuritiesDataAnalysisPython/tree/main/code/Investment_Strategy)

Harry Max Markowitz가 구축한 현대 포트폴리오 이론부터 듀얼 모멘텀 전략까지 다양한 전략을 구현함.

* [Efficient Frontier(완료)](https://github.com/inandout-kr/SecuritiesDataAnalysisPython/blob/main/code/Investment_Strategy/Efficient_Frontier.py) [(Jupyter)](https://github.com/inandout-kr/SecuritiesDataAnalysisPython/blob/main/code/Investment_Strategy/Efficient_Frontier(Jupyter).ipynb)
* 볼린저 밴드를 이용한 추세 추종, 반전 매매기법
* 삼중창 매매기법
* 듀얼 모멘텀 전략(상대 + 절대 모멘텀)

