# <img src="https://cdn.emojidex.com/emoji/seal/youtube.png" width=10% height=10%> 3Team의 웹 개발 프로젝트 : ALPHATUBE 
--------------------------------------
# <img src="https://pic.sopili.net/pub/emoji/twitter/2/72x72/2049.png" width=30 height=30>QUESTION.왜 이 프로젝트를 진행하게 되었나요 ? #
+ 기업의 마케팅 분야에서 가장 많이 활용되는 것이 바로 데이터 분석을 통한 추천 알고리즘!
+ 고객의 NEEDS에 대해 상품을 제안하는 것 중 우리에게 가장 익숙한 동영상 OTT 플랫폼!
+ 시청자와 쌍방향의 소통이 가능하다는 강점!
+ 키워드 접근으로 남녀노소 접근이 용이한 접근성!
+ 그래서 남녀노소가 즐겨보는 유튜브 플랫폼을 참고해서 개발!
--------------------------------------
 # <img src="https://pic.sopili.net/pub/emoji/twitter/2/72x72/1f4bb.png" width=30 height=30>개발 환경 #
+ GitHub
+ Pycharm
+ Mysql
----------------------------------------
# <img src="https://pic.sopili.net/pub/emoji/twitter/2/72x72/1f5d2.png" width=30 height=30>구현한 기능 #
+ 로그인/회원가입
+ 로그아웃
+ 카카오 로그인,로그아웃
+ 썸네일,동영상 업로드, 수정, 삭제
+ 관리 페이지 운용
+ 구글 애널리틱스 API
+ 카테고리(태그)에 의한 분류
+ 비슷한 카테고리(태그)에 해당하는 추천 영상
+ 댓글의 등록
+ 익명성 배제

------------------------------------
# 📂사용한 라이브러리 #
+ Django
+ Pillow
+ google_analytics
+ mysqlclient
+ oauth2client
+ google-api-python-client
+ sqlparse
-------------------------------------
# 📓사용한 기술 #
## ✋BACKEND ##
+ Python
+ Mysql
+ Django
+ ORM
-------------
## 🤚FRONTEND ##
+ Javascript
+ CSS
+ Html
--------------------------------------
# ERD와 서버 Architecture #
## ERD 설계 ##
![ERD](https://user-images.githubusercontent.com/97925049/151302210-5db7af27-5efe-4c96-8936-4f8d3fc98f34.png)
-----------------
## SERVER ARCHITECTURE ##
![아키텍쳐](https://user-images.githubusercontent.com/97925049/151467213-892d76ce-7400-4fdf-b66c-583619c01ba4.png)
-----------------------------------
# 🆖개발하면서 어려운 점과 개선할 부분🆖 #
--------------------------------
## 어려웠던 점 ##
+ 로그인/회원가입에서 데이터의 연동, 관계 테이블 값의 출력
+ 댓글에서 입력에서 출력까지의 과정
+ 영상에서 자주 찾는 영상 카테고리의 정렬
+ 구글api서비스에서 특정키를 통해 데이터를 뽑아오는 과정에서 해당 코드에 대한 이해도의 부족
+ 처음 DB 저장에서 찾기를 위한 테이블 지정의 실수
---------------
## 개선할 부분 ##
+ 로그인/회원가입에서 카카오 로그인 시 동의항목에서 이메일 선택하지 않으면 오류뜨는 부분
+ 로그인/회원가입에서 아이디 찾기와 비밀번호 찾기의 분리
+ 비밀번호 찾기 기능을 비밀번호 변경으로 구현했는데 비밀번호 찾기로 구현의 필요
+ 댓글에서 댓글창과 폰트의 심미성
+ 댓글에서 대댓글 구현
+ 댓글에서 댓글의 공감 구현
+ 영상에서 자주 찾는 영상 카테고리 정렬과 카테고리의 세분화
+ DB에서 저장된 이메일이 있으면 코드를 전송하고 서버에서 보낸 코드와 사용자가 입력한 코드가 맞으면 DB에 저장된 사용자의 아이디를 찾고 패스워드를 바꿀 수 있게 수정
+ 업로드한 영상 수정에 있어서 모든 값을 넣어야 되는 부분을 수정
+ 구글애널리틱스 api에서 원하는 데이터를 get하기
---------------------------
# <img src="https://pic.sopili.net/pub/emoji/twitter/2/72x72/231b.png" width=40 height=40>참조
+ Youtube
+ Google
