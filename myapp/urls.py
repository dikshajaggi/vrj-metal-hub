from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name="home"),
    path('prodCat/', views.prodCat, name="prodCat"),
    path('desc/<str:id>/' , views.desc , name ='desc'),
    path('form/' , views.form , name ='form'),
    path('about/' , views.about , name ='about'),
    path('offers/' , views.offers , name ='offers'),
    path('newArrivals/' , views.newArrivals , name ='newArrivals'),
    
]
