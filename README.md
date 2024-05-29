# Hands_MediaPipe_project


## 5/23(목)
> - Postgres 사용하여 test 데이터베이스 생성
> - 임시 구축된 서버에 생성한 test 데이터베이스 연동(create 눌렀을 때 데이터 DB에 들어오는지 확인)

## 5/24(금)
> - test 데이터베이스를 관계형 데이터베이스로 변환(웹 서버 로그를 DB와 연동)
> - 웹 서버 로그를 DB와 연동 시 웹 페이지가 로그가 찍히는 JSON파일과 동일하게 로그 화면으로 바뀌는 문제 발생.
> - 로그가 2개씩 찍히는 문제 발생.

## 5/27(월)
> - @app.after_request에 if response.content_type == 'application/json': 으로 if문 걸어줌으로써 홈페이지 화면이 로그 화면으로 바뀌는 문제 해결.
> - app.run의 debug=True를 제거하니 로그가 2개씩 찍히는 문제 해결.
> - 그러나 로그가 찍힐 때마다 JSON파일로 바로 전달되는 것이 아니라 지연되어 저장되는 문제 발생 -> 네트워크 문제일 가능성이 높다고 판단되어 코드 수정 없이 그대로 유지하기로 함.

## 5/28(화)
> - Google Cloud Postgresql를 로컬 DB와 연결
> - 새로 구축된 웹 서버와 로컬 DB 연동

## 5/29(수)
> - 테이블 정의 다시 함(id 컬럼과 time 컬럼을 primary key로 지정해서 중복된 값을 받아와도 문제 없도록 수정).
> - 행동 로그 추출(label, id, coordinate, time, ...)
> - 새로운 가상 환경 구축(python -> conda)
