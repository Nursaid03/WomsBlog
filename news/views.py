from django.shortcuts import render, get_object_or_404
from .models import News

def new_list(request):
    """Вывод всех новостей
    """
    news = News.objects.all()
    return render(request, 'news/news_list.html', {'news': news})

def new_single(request, pk):
    """Вывод полной статьи
    """
    new = get_object_or_404(News, pk=pk)
    return render(request, 'news/news_single.html', {'new': new})
