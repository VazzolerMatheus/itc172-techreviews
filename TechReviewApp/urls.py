from django.urls import path

from . import views


#study

urlpatterns=[

    #path is a newer version of url

    path('', views.index, name='index'), 
    
    path('getTypes/', views.getTypes, name='types'),

    path('getProducts/', views.getProducts, name='products')

    
]