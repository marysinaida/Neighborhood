from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name='index'),
    url('^today/$',views.news_of_day,name='newsToday'),
    url(r'neighborhood/(\d+)',views.neighborhood,name='neighborhood'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^hood/(?P<id>\d+)/', views.hood, name='hood'),
    url(r'^new/neighborhood$', views.new_neighbor, name='new-neighbor'),
    url(r'^post/(?P<id>\d+)', views.add_post, name='new_post'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
         
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)