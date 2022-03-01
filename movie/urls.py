from django.urls import path 
from . import views 

#app_name = "movie"
urlpatterns = [
    path('',views.home, name="home"),
    path('success',views.success, name="success"),
    path('rate/<int:id>',views.rate,name="rate"),
]
