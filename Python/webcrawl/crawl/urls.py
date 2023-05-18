from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('search/', views.search, name="search"),
    path('bieudothuonghieu/', views.bieudothuonghieu, name="bieudothuonghieu"),
    path('bieudosanpham/', views.bieudosanpham, name="bieudosanpham"),
    path('bieudocuahang/', views.bieudocuahang, name="bieudocuahang"),
    path("/<int:pk>",views.Category.as_view(), name= "category"),
    path("todo/",views.todo, name="todo")
]