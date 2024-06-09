from django.urls import path
from . import views
app_name = 'myapp'
urlpatterns = [
    path('', views.idcard_home),
    path('home', views.home_page, name='home_page'),
    path('createCard/<str:cardName>', views.createCard, name="createCard"),
    path('idcard_download/<str:unique_id>/', views.idcard_download, name='idcard_download'),
]
