from django.urls import path  #path is just a default django function used to configure urls 
from . import views 

urlpatterns=[
    path('',views.index,name='index'),
    path('post/<str:pk>',views.post,name='post')
]