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