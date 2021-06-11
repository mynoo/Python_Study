# Web crawling

- 각 치킨 매장의 지점 주소를 웹 페이지에서 크롤링
  - 각 크롤링 한 파일들을 allstore.csv 파일에 종합(chickenConcat.py 파일에서 실행)
    - 처갓집 : http://www.cheogajip.co.kr/bbs/board.php?bo_table=store
    - 굽네치킨 : http://www.goobne.co.kr/store/search_store.jsp
    - 네네치킨 : https://nenechicken.com/17_new/sub_shop01.asp
    - 페리카나 : https://www.pelicana.co.kr/store/stroe_search.html

<br>

- Selenium
  - filename : seleniumTest01.py
    - google 홈페이지를 연다.
    - 북미정상회담을 검색한다.
    - 해당 검색창 캡쳐 후 파일 저장
    - Browser 종료한다.
<br>

- 네이버 웹툰 홈페이지 요일별 크롤링
  - 주소 : https://comic.naver.com/webtoon/weekday.nhn
    - 요일, 웹툰명, 이미지링크 정보 추출
    - 요일별 이미지 저장
