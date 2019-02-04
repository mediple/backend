# 메디플 백엔드

## 개요

responder로 구현한 RESTapi 서버입니다.

## 본 프로젝트 사용법

1. git clone "https://github.com/mediple/backend.git"<br><br>
2. cd backend<br><br>
3. mkdir .secret<br><br>
4. 아래와 같이 프로젝트 루트에 파일 생성<br><br>
 .secret<br>
┗━━━ info.json<br><br>
<pre>{
  "mediple": {
    "database": {
      "url" : "데이터베이스 url"
    }
  }
}</pre>