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
## 어려웠던 점과 해결 ##
+ 1:1로 연결된 테이블에서 원하는 값 추출하는 방법
* 해결방안 : 서로 다른 테이블에서 원하는 값을 추출할 때 사용하는 조인 방법을 사용해서 해결
+ 구글API서비스를 사용하면 원하는 데이터를 뽑아낼 수 있지만 키와 데이터의 연결관계를 파악하지 못함
* 해결방안 : 구글애널리틱스 demos & tool을 통해 디멘션과 매트릭스 항목에서 특정키를 선택했을 때 추출될 데이터를 미리 확
인할 수 있었고 특정키를 하나하나 바꿔보는 과정을 거치면서 원하는 데이터와
연결된 키를 찾아낼 수 있었고 이를 코드로 작성해서 데이터를 출력
+ 댓글 입출력의 어려움
* 해결방안 : 동영상 부분을 담당한 팀원의 views에 함수를 다시 정의해서 메인페이지에 출력될 수 있게 함
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
# 역할 분담 #
## 박영후 ##
+ DB 생성 및 총괄
## 양정헌 ##
+ 댓글조회, 댓글 업로드
## 장규호 ##
+ 동영상 업로드, 분류
## 한재리 ##
+ 로그인,회원가입,카카오 로그인 API
--------------------------
# <img src="https://pic.sopili.net/pub/emoji/twitter/2/72x72/231b.png" width=40 height=40>참조
+ Youtube
+ Google
