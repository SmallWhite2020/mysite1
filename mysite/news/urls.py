from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'articles/<int:year>/', include('views.year_archive')),
    # url(r'articles/<int:year>/<int:month>/', include('views.month_archive')),
    # url(r'articles/<int:year>/<int:month>/<int:pk>/', include('views.article_detail')),
    # url(r'articles', views.welcome),
    url('', views.welcome)

]