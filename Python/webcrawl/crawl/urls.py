from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home,name="home"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.register, name="register"),
    path('search/', views.search, name="search"),
    path('bieudothuonghieu/', views.bieudothuonghieu, name="bieudothuonghieu"),
    path('bieudosanpham/', views.bieudosanpham, name="bieudosanpham"),
    path('bieudocuahang/', views.bieudocuahang, name="bieudocuahang"),
    path("/<int:pk>",views.Category.as_view(), name= "category"),
    path("categories/info/<int:pk>",views.Todo.as_view(), name= "todo"),
    path('upload/', views.import_view, name="upload"),
]