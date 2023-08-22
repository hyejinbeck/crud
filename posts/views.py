from django.shortcuts import render, redirect
# Post 모델(클래스/기능이있음) 을 import 불러온다. 
from .models import Post

# Create your views here.
def index(request): 
    posts = Post.objects.all()
    
    context = {
        'posts' : posts, 
    }

    return render(request,'index.html',context)

def detail(request, id):
    post = Post.objects.get(id=id)
    # id가 id인 애를 가져와! 

    context = {
        'post': post, 
    }

    return render(request, 'detail.html', context)



def new(request): 
    return render(request, 'new.html')

def create(request): 
    title = request.GET.get('title')
    content = request.GET.get('content')

    post = Post()
    post.title = title 
    post.content = content 
    post.save()

    return redirect(f'/posts/{post.id}')

def delete(request,id): 
    post= Post.objects.get(id=id)
    post.delete()

    return redirect('/index/')

def edit(request, id): 
    post = Post.objects.get(id=id)
    
    context= {
        'post': post,
    }
    
    return render(request, 'edit.html',context)

def update(request, id): 
    # 방금 수정한 데이터 
    title = request.GET.get('title')
    content = request.GET.get('content')

    # 기존데이터 
    post = Post.objects.get(id=id)
    post.title = title 
    post.content = content
    post.save()

    return redirect(f'/posts/{post.id}')


