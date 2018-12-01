from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('our_story', views.our_story, name='our_story'),
    path('portfolio', views.portfolio, name='portfolio'),
    #should later add on get ID<id>
    path('portfolio/detail_1', views.portfolio_detail_1, name='portfolio_detail_1'),
    
        

]
