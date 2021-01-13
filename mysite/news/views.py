
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse


from .models import Article

print('views')

# def year_archive(request, year):
#     a_list = Article.objects.filter(pub_date__year=year)
#     context = {'year': year, 'article_list': a_list}
#     # return render(request, 'news/templates/year_archive.html', context)
#     return render(request, 'news/templates/1.html', context)


def welcome(request):
    return HttpResponse("<h1> Welcome to my tiny twitter2222! </h1>")
