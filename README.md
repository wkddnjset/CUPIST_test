# CUPIST_test

### 코드 실행하기

- **Python 환경설정**<br/><br/>
  - Python 3.6 버전으로 `venv`라는 가상환경을 만들고 해당 경로에서 아래명령을 실행시킨다.

```bash
(venv)Project\CUPIST_test> pip install -r requirements.txt
```

- **Django 실행**<br/><br/>
  - 라이브러리 설치가 끝나면 src폴더로 이동해 아래명령을 실행시킨다.
  
```bash
(venv)Project\CUPIST_test\src> python manage.py runserver
```
> 관리자페이지 : localhost:8000/admin <br/>
> 홈페이지 : localhost:8000/

### 코드 설명

- **src/CoupleManager/models.py**<br/><br/>
  - 장고의 **MTV**구조에서 **M(Model)**을 담당<br/>
  - Male, Female **모델 클래스** 정의<br/>
  - 각 필드에 **validation함수**를 만들어 적용<br/>
  - `pre_save`를 사용해 입력받은 취미를 **List**로 재입력<br/>
  - `posr_save`를 사용해 저장된 데이터 **Json형태**로 출력<br/>
  
- **src/CoupleManager/views.py**<br/><br/>
  - 장고의 **MTV**구조에서 **V(View)** 를 담당<br/>
  - **CoupleManager**라는 클래스를 만들어 기능수행<br/>
  - `template_name`을 사용해 **프런트와 연결**<br/>
  - Template에서 GET으로 받아온 데이터를 CoupleManager클래스에 **파라미터**로 넘겨 <br/>출력된 텍스트를 **Json형식**으로 **Return**<br/>
  - Male, Female에 대한 값을 받아오지 못하면 {"error":"True"} 값을 넘겨 **Validation 수행**<br/>

- **src/CoupleManager/views.py**<br/><br/>
  - 장고의 **MTV**구조에서 **V(View)** 를 담당<br/>
  - **CoupleManager**라는 클래스를 만들어 기능수행<br/>
  - `template_name`을 사용해 **프런트와 연결**<br/>
  - Template에서 GET으로 받아온 데이터를 CoupleManager클래스에 **파라미터**로 넘겨 <br/>출력된 텍스트를 **Json형식**으로 **Return**<br/>
  - Male, Female에 대한 값을 받아오지 못하면 {"error":"True"} 값을 넘겨 **Validation 수행**<br/>
  
- **src/CoupleManager/urls.py**<br/><br/>
  - view에 대한 url설정을 해주는 곳<br/>

- **src/CoupleManager/admin.py**<br/><br/>
  - models.py에서 정의한 테이블을 관리자페이지에서 볼 수 있도록 설정<br/>


- **src/templates/snippets**<br/><br/>
  - 글로벌하게 설정하고 싶은 Javascript 혹은 CSS에 대한 내용<br/>

- **src/templates/base.html**<br/><br/>
  - 위에서 설정한 값을 모두 포함한 html 틀<br/>
  - Tamplate Tag를 사용<br/>
 
- **src/templates/CoupleManager/list.html**<br/><br/>
  - views.py에서 정의한 UserList 뷰 클래스와 연결되는 프런트엔드<br/>

- **src/templates/CoupleManager/list_js.html**<br/><br/>
  - list.html에서 선택하기 버튼 클릭에 대한 스크립트 정의<br/>
