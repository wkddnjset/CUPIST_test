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
  - Template에서 GET으로 받아온 데이터를 CoupleManager클래스에 **파라미터**로 넘겨 출력된 텍스트를 **Json형식**으로 **Return**<br/>
  - Male, Female에 대한 값을 받아오지 못하면 {"error":"True"} 값을 넘겨 **Validation 수행**<br/>
  

  
