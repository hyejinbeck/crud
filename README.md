**CRUD**
`Create` 게시판 만들고 
`Read` 읽기
`Update` 업데이트하기 
`Delete` 삭제하기 

# 새 폴더 만들고 초기셋팅 

- 새 폴더 생성 
- vs코드 실행 
- .gitignore 생성 
- Django 프로젝트 생성 

vs코드 터미널에서 django-admin startproject crud .
```
여기서 . 은 필요함. 
crud 는 생성한 폴더 이름을 뜻함 
```

- 가상환경 설정 python -m venv venv   
- 가상환경 설정화 source venv/bin/activate
- 가상환경에 django 설치 
pip install django
- 그리고 git init 
- 그리고 git add .gitignore README.md  
- 그리고 git commit -m '프로젝트 폴더 셋팅/ git / README'
- 그리고 git add . 또는 git add crud/ manage.py 
- 그리고 git commit -m 'django-admin startproject' 

`tip` : 틈틈히 commit 할때 어떤 걸 구현했는지 추가 기재해줄 것 

- django 프로젝트 실행 확인 python manage.py runserver 
로켓 나오면 정상 

- app 하나 만들기 
django-admin startapp posts

- urls에 추가 
from 폴더명 import views
그리고 밑에 urlpatterns 에 추가 
path('index/', views.index)
index를 요청하면 index파일을 보여줘라는 내용 

- views index파일 요청시, 보여줄 내용 기재 
def index(request): .. 

- posts폴더에 templates 폴더 생성후, index.html 파일 만들기 

- 만들어진 index.html 에 ! 누르고  tab 눌러 셋팅 
- 그리고 보여줄 내용 기재 

- 다 저장한 뒤, 로켓트가 나온 django 웹 본 뒤 /index 눌러 잘 실행되는지 확인 