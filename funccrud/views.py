from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog

# Create your views here.
def welcome(request):
    return render(request, 'index.html')

def read(request):
    blogs = Blog.objects.all()
    return render(request, 'funccrud.html',{'blogs':blogs})

def create(request):
    #새로운 데이터 새로운 블로그 글 저장하는 역할 == POST
    if request.method == 'POST':
        post = Blog()
        post.image = request.FILES['p']
        post.title = request.POST['t']
        post.body = request.POST['b']
        post.pub_date = timezone.now()
        post.save()
        return redirect('home')
    else:
        return render(request,'create.html')
    

def update(request, pk):
    #어떤 블로그를 수정할지 블로그 객체를 갖고오기
    blog = get_object_or_404(Blog, pk = pk)

    if request.method == 'POST':
        blog.image = request.FILES['p']
        blog.title = request.POST['t']
        blog.body = request.POST['b']
        blog.save()
        return redirect('home')
    else:
        return render(request, 'update.html', {'blog':blog})

def delete(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    blog.delete()
    return redirect('home')

def detail(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    #이용자가 원하는 몇번 객체
    
    return render(request, 'detail.html', {'blog':blog})