from django.urls import path
from.import views

urlpatterns = [
 path('', views.home, name='home'),
 path('about/', views.about, name='about'),
 path('autos/', views.autos_index, name='index'),
 path('autos/<int:auto_id>/', views.autos_detail, name='detail'),
]

