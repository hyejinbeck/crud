
# 프로젝트 구조 작성 
>1. 셋팅(app생성까지)
>2. 모델(DB)
>3. CRUD

# 1. 셋팅 
### 1. 프로젝트 폴더 생성 
### 2. 프로젝트 폴더로 이동해서 VScode실행 
### 3. `.gitignore` 파일 생성 -> gitignore.io 사이트 
### 4. `README.md` 파일 생성
### 5. django 프로젝트 생성 
```bash
django-admin startproject 프로젝트명 엔터한칸 . 꼭 해야함 
특히 . 안하면 폴더 추가로 한개 더 생성됨. 
```
### 6. 가상환경 설정과 활성 
```bash
python -m venv venv
source venv/bin/activate
```
윈도우에서는 bin대신 Script <br>
(venv)(base)가 되면 성공적! 

### 7. 가상환경에 django설치 
```bash
pip install django
```

### 8. 여기즈음에서 github연동하자. 
```bash
git init 
git add .gitignore README.md 
git commit -m "프로젝트 폴더 셋팅/git 과 README" 
git add 프로젝트명/manage.py 
git commit -m "django-admin startproject"

그리고 github 사이트의 new repo만들어서 연결-등록
```

### 9. django정상적으로 실행되는지 확인
```bash
python manage.py runserver
```
`http://127.0.0.1:8000/` 눌러서 로켓 나오면 성공적! <br>
ctrl + c 하면 django 종료 할 수 있는데, <br>
그냥 하단의 터미널창을 하나 더 켜서 병행하자. 

### 10. 앱 생성 
```bash
django-admin startapp 앱이름
```
그럼 앱이름으로 폴더 생성된다. 

### 11. 앱 등록 
`settings.py`에 앱이름 추가
```bash
INSTALLED_APPS = [
    ...
    <app_name>, 
]
```
`urls.py`에 2가지 추가 
```bash
상단 
from 앱이름 import views 

하단 urlpattern = 
path('index/',views.index), 
```
`views.py`에 def함수로 기능 서술 
```bash
def index(request): 
    return render(request,'index.html')
```
`앱이름`폴더안에 `templates`폴더 생성 -> `index.html`파일 생성 <br>
`index.html` 파일에 ! 누르고 tab 하여 폼 생성 
```bash
<body>
    <h1>index</h1>
</body>
```

### 12. 앱등록완료, 실행 확인 
아까 로켓나오던 사이트 새로고침하면 <br>
`index.html` 기재내용 나온다. 

# 2. 모델 
모델링을 한다<br>
= 스키마를 정의한다

### 1. `model.py` 로 모델 정의
class함수 생성 한다. <br>
기본적으로, 클래스이름(모델)은 단수형태이다. 
<br>
django의 models 안에 있는 Model이라는 클래스를 인자로 받아오자.
```bash
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
```
게시물을 기재하는 Post클래스를 생성 <br>
제목는 짧은 글자 작성하게 <br>
내용에는 좀 더 긴글자 작성하게 라는 내용이다. 

### 2. `make migrations` 번역본 생성 
```bash
python manage.py makemigrations
```
앱이름>migrations>`0001_initial.py`생성된다. 

### 3. `migrate` DB에 반영 
```bash
python manage.py migrate
```

### 4. SQL 스키마 확인
```bash
python manage.py sqlmigrate posts 0001
```

### 5. `admin.py` 생성모델 admin등록 
```python
from django.contrib import admin
from .models import Post   # 이거 추가 
# Register your models here.

admin.site.register(Post)   # 이거 추가 
# Post라는 클래스를 관리자페이지에 등록해주세요.
```

### 6. `createsuperuser`관리자계정 생성
```bash
python manage.py createsuperuser
```
username, Email address, Password 입력 

### 7. 관리자계정 로그인 후 게시글 작성
```
http://127.0.0.1:8000/admin 치고 엔터 
```
Django administration 나오면 성공적 
```
Posts > add > Title과 Content 입력
```
지금은 제목이 Post object(n..)으로 나온다. 

# 3. CRUD 
게시물(post)을 읽고,만들고,삭제하고,업데이트해보자. 

## 1. Read의 종류
> 1. 모든 페이지의 title 출력
> 2. 1개의 상세페이지 출력
> 3. 각 게시물 제목에 detail링크추가

## 1.1 Read(all): 모든페이지
### 1. `index.html` 에 기재 
위의 모델(클래스)를 DB에서 불러오고, index.html로 보여줘.
```python 
<body>
    <h1>index</h1>
    {% for post in posts %}
        <p>{{  post }}</p>
    {% endfor %}
</body>
```
### 2. `views.py` 에 기재 
보여주는 기술에 대해 서술 <br>
index 함수에 `모든 게시물을 읽어오는 변수` 추가 
```python 
from django.shortcuts import render
from .models import Post   # 기재 

# Create your views here.
def index(request): 
    posts = Post.objects.all()  # 기재 
    #  변수= 모델클래스이름.모든걸 보여줘()
    #  변수에 담아 데이터를 가져온다. 
    context = {
        'posts': posts,
        # 내용 = 모든 게시글 
    }
    return render(request,'index.html',context)
```
### 3. `여기까지 확인`
http://127.0.0.1:8000/index/ <br>
하게되면 출력시, <br>
**index** <br>
첫번째게시글 제목<br>
두번째게시글 제목<br>
.. 등등 <br>
## 1.2 Read(n) : 1개의 상세페이지
### 1. `urls.py`
posts/몇번째 게시글인지 추가 + index말고 detail에서 보여줘.
```python
urlpatterns = [
    ... 
    path("posts/<int:id>/",views.detail),
]
```
id에는 post게시글의 몇번째 순서인지 값이 주워지고,<br>숫자이기 때문에 int를 해야 error가 안생긴다. 
### 2. `views.py`
```python
def detail(request, id):    # id값 추가 
    post = Post.objects.get(id=id)
                     # 상세는 get(id=id)
    context = {
        'post': post,
        # 위에와는 달리 post단수로 쓰인다.
    }

    return render(request, 'detail.html', context)
```
### 3. `detail.html`생성 
templates>detail.html생성 <br>
! 하고 tab 하여 폼 불러오기 
```python
<body>
    <h1>{{post.title}}</h1>
</body>
```
### 여기까지 확인 
http://127.0.0.1:8000/posts/2/<br>
/posts/몇번째 게시글인지 번호
```python
<h1>{{post}}</h1>는 detail.html에서 
Post object (n) 
이러한 형식으로 출력됨.

<h1>{{post.title}}</h1>detail.html에서
각 게시물제목의 실제제목이 출력됨. 
```

## 1.3 index 각 게시물 제목에 링크 추가
### 1. `index.html` 에 `detail`링크 추가
```python 
<body>
    <h1>index</h1>
    {% for post in posts %}
        <p>{{  post.title }}</p>
        <a href="/posts/{{post.id}}">detail</a>       # 추가 
        <hr>
    {% endfor %}
</body>
```
```
<a>태그: 링크 걸수 있다. 
href="링크주소"
http://127.0.0.1:8000/posts/1 와
                     /posts/1는 같다. 
> 보여지는 링크명 < 

<hr>태그: 구분선 
markdown의 --와 같다. 
```
### 2. `detail.html`링크후 페이지 내용물
위의 index에 나오는 게시물 제목들 아래에 detail링크들을<br>
누르면 내용물을 볼 수 있는 상세페이지로 들어가게 해보자.
<br> `detail.html`
```python
<body>
    <h1>{{post.title}}</h1>
    <p>{{post.content}}</p>  # 추가기재 
</body>
```
다시 정리하자면, <br>
index.html은 게시물의 제목목록+detail링크<br>
`/index/`검색해야함<br><br>
detail.html은 게시물의 상세페이지이며, <br>
각 게시글의 제목과 내용이 나온다. 
`/posts/1/`검색하거나, index에서 링크타고<br>

### 3. 확인 
http://127.0.0.1:8000/index/ 

## 2. Create 
>1. 사용자가 입력하는 폼을 만들고 
>2. 입력한 데이터를 DB에 저장

## 2.1 사용자 입력 폼 `new`
### 1. `urls.py`
```python 
urlpatterns = [
    ...
    path("posts/new/",views.new),
]
```
`" "`:url사이트 주소창에 검색하는 경로<br>
`,views.new`: 뭘 실행시킬지  
### 2. `views.py`
```python
def new(request): 
    return render(request,'new.html')
```
### 3. `templates`->`new.html`생성
! 누르고 tab 해서 셋팅 <br>
`과정설명1`
```python
<body>
    <h1>new</h1>

    <form action="">
    # 입력값을 받은뒤,뭘 할지 아직 안만듬.
        <input type="text"> 
        # 사용자 입력할수 있는 네모박스
            # 이제 여기에 title 입력값으로 부여해주자.
        <textarea name="" id="" cols="30" rows="10"></textarea>
        # 사용자 입력할수있는 더 큰 네모박스
            # 이제 여기에 content 입력값으로 부여해주자. 
        <input type="submit">
        # 조그만한 네모[제출] 누를 수 있음. 
    </form>
</body>
```
`과정설명2`
```python
<body>
    <h1>new</h1>

    <form action="/posts/create">
            # 입력값을 받으면, create로 넘어가게할거야.(아직안만듬)
        <input type="text" name="title">
            # 여기 입력값을 title로 해주자.
        <textarea name="content" id="" cols="30" rows="10"></textarea>
            # 여기 입력값을 content로 해주자.
        <input type="submit">
    </form>
</body>
```
http://127.0.0.1:8000/posts/new/ <br>
이상태에서 실행은 불가함 -> 아직 create 안만듬

## 2.2 사용자 입력값 DB에 저장 `create`
### 1. create 동작 추가 
`urls.py`
```python
urlpatterns = [
    ...
    path("posts/create/",views.create)
]
```
`views.py`: 내가 꺼내오고 싶은 값 함수 생성
```python
from django.shortcuts import render #여기에 뒤에 , redirect 추가 
```
```python
def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    post = Post()        # 변수에 저장
    post.title = title     # 제목
    post.content = content  # 내용
    post.save()        # 그리고 DB에 저장

    return redirect(f'/posts/{post.id}/')
    # 사용자입력new게시글의 상세페이지로 이동
```
### 2. 순서정리 
```python
1. urls.py -> new 입력값 셋팅
사용자가 게시물 추가하기위해 /posts/new 검색

2. views.py -> def new 
생성하기위해 만들어진 new포멧으로 이동후, 
new.html로 이동시켜줘서 바꿀 값과 매칭하게해줌 

3. new.html -> submit 제출버튼
추가생성할 내용 기재 
제목,내용,제출버튼 

4. urls.py -> create입력값 셋팅 
사용자가 기재한 내용을 만들어주는 /posts/create 

5. views.py -> def create
추가기재한 내용들을 따로 저장한다. 
제목은 제목 
내용은 내용 
그리고 DB에 저장해서 redirect로 이동 

/posts/추가생성되어 몇번째 게시물인지 보여줌 
```
### 3. 확인 
사용자가 게시물 생성하기위해 new <br>
http://127.0.0.1:8000/posts/new/
<br> 제목입력칸, 내용입력칸 그리고 [제출]
<br> 
<br> 출력내용 : 제목, 내용 
<br> url주소: http://127.0.0.1:8000/posts/몇번째인지/

## 3. Delete 
### 1. `urls.py` 지워줘 요청 
```python 
urlpatterns = [
    ...
    path("posts/<int:id>/delete/",views.delete),
]
```
### 2. `views.py` 
지워야하는 요청값 찾기->없애기->redirect이동(index로)
```python
def delete(request, id):            # delete요청 구현
    post = Post.objects.get(id=id)    # 값 찾기 
    post.delete()                      # 없애기 

    return redirect('/index/')       # 없애고 index이동
```
이상태에서는 사용자가, 굳이 index로 게시물->detail링크타고 <br>
상세페이지로 가서 url사이트주소에 `/delete`기재해야 삭제된다.<br>
`delete` 버튼도 만들어보자. 

### 5. `detail.py` delete 버튼추가
```python
<body>
    <h1>{{post.title}}</h1>
    <p>{{post.content}}</p>

    <a href="/posts/{{post.id}}/delete">delete</a> # 추가 
</body>
```
`<a>`태그는 버튼 만들어주는 태그 <br>
href="버튼누르고 그 기능이 적용되는 사이트주소"

### 4. 확인 
http://127.0.0.1:8000/index/ 에서 <br>
삭제원하는 게시글 [detail]링크 눌러 상세페이지로 이동<br>
http://127.0.0.1:8000/posts/2/delete 엔터치면 삭제 <br>
또는 <br>
내용 하단의 delete 링크 누르면 삭제 후<br>
http://127.0.0.1:8000/index/ 로 이동ok 

## 4. Update 
> 기존데이터를 담은 form 제공 -> edit 으로 불러오기 
> 기존데이터에 추가/삭제/변경사항 기재 가능 


### 1. edit -> `url.py` 
```python
urlpatterns = [
    ...
    path('posts/<int:id>/edit/', views.edit),
]
```
### 2. edit -> `view.py` 
```python 
def edit(request, id): 
    post = Post.objects.get(id=id)
    
    context= {
        'post': post,
    }
    
    return render(request, 'edit.html',context)
```
### 3. edit -> `edit.html`
tempalte 폴더 > edit.html 생성 <br>
! 그리고 tab 해서 셋팅 후 기재  
`과정설명1`
```python
<body>
    <h1>edit</h1>

    <form action="">
        <input type="text">    # 제목 수정 가능하게끔 
        <textarea name="" id="" cols="30" rows="10"></textarea>   # 내용 수정 가능하게끔
        <input type="submit">   # 제출버튼 
    </form> 
</body>
```
`과정설명2`
```python
<body>
    <h1>edit</h1>

    <form action="">
        <input type="text" value="{{post.title}}">
        <textarea name="" id="" cols="30" rows="10">{{post.content}}</textarea>
        <input type="submit">
    </form>
</body>
```

### 4. edit -> `detail.html` 버튼추가 
```python
<body>
    <h1>{{post.title}}</h1>
    <p>{{post.content}}</p>

    <a href="/posts/{{post.id}}/delete">delete</a>
    <a href="/posts/{{post.id}}/edit">edit</a> # 추가
</body>
</html>
```
### 5. edit -> `url.py` 수정값 실행url
```python
urlpatterns = [
    ...
    path('posts/<int:id>/update/',views.update),
]
```
### 6. edit -> `views.py` 수정값 실행내용
제목과 내용에 각각 내용 수정후 -> 제출버튼 누르면 <br>
그 변경된 데이터값을 어떻게 구현해서 보여줄건지 
```python
def update(request, id):
    # 방금 수정한 데이터를 기존데이터에 덮어씌운다.
    title = request.GET.get('title')
    content = request.GET.get('content')

    # post = Post() => 새로운 게시물 만들때쓰며
    # 지금처럼 edit,update할때는 부필요하다.
    # 기존데이터
    post = Post.objects.get(id=id)
    post.title = title
    post.content = content
    post.save()

    return redirect(f'/posts/{post.id}/')
``` 
### 7. edit -> `edit.html` 새데이터값으로 보여주기
`진행과정1`
```python
<body>
    <h1>edit</h1>

    <form action=" #수정본을 보여줄 새로운url주소로 이동  ">
        <input type="text" value="{{post.title}} # 그리고 여기에 title 부여해주기">
        <textarea name=" # 여기에 content 부여해주기" id="" cols="30" rows="10">{{post.content}}</textarea>
        <input type="submit">
    </form>
</body>
``` 
`진행과정2`
```python
<body>
    <h1>edit</h1>

    <form action="/posts/{{post.id}}/update">
        <input type="text" value="{{post.title}}" name="title">
        <textarea name="content" id="" cols="30" rows="10">{{post.content}}</textarea>
        <input type="submit">
    </form>
</body>
``` 
### 8. 구현 확인 
http://127.0.0.1:8000/index/ <br>
원하는 게시글의 detail 눌러 상세페이지로 이동 <br>
상세페이지의 delete, edit버튼중 edit 눌러서 이동<br>
[기존제목값],[기존내용값]그리고 제출버튼 <br>
제목과 내용을 각각 수정한 뒤, 제출버튼 누른다. <br>
변경되었는지 확인 ok 
