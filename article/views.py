from django.shortcuts import render, redirect
import random
from .models import Article

# Create your views here.
# 
def index(request):
    return render(request, 'index.html') 
    
def dinner(request):
    menus = [{ 'name':'족발', 'price':20000}:,{'name':'햄버거', 'price':10000},{'name':'피자', 'price':20000},{'name':'초밥', 'price':15000}] #dictionary 자료형    pick = random.choice(menus) #menus에서 임의로 추출
    articles = Article.objects.all() #모든 article을 불러오라고 명령하는 선언
    context = { #html에 가져갈 데이터를 정의, pick, name(urls.py), menus 3개를 지정        
        'pick' : pick,        
        'menus' : menus,
        'articles': articles,    
    }    
    return render(request, 'dinner.html', context)


def create_review(request):
    content = request.POST.get('content')
    title = request.POST.get('title')
    article = Article(title=title, content=content)
    article.save()

    return redirect('articles:detail', article.pk)

def detail(request, pk):
    article = Article.objects.get(pk:pk)
    context = {
        'article' : article,
    }
    return render(request, 'detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk, pk)
    
    if request.method == 'POST':
    article.delete()
    
    return redirect('articles:dinner')