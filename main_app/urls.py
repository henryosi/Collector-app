from django.urls import path, include
from.import views

urlpatterns = [
 path('', views.home, name='home'),
 path('about/', views.about, name='about'),
 path('autos/', views.autos_index, name='index'),
 path('autos/<int:auto_id>/', views.autos_detail, name='detail'),
 path('autos/create/', views.AutoCreate.as_view(), name='autos_create'),
 path('autos/<int:pk>/update/', views.AutoUpdate.as_view(), name='autos_update'),
 path('autos/<int:pk>/delete/', views.AutoDelete.as_view(), name='autos_delete'),
 path('autos/<int:auto_id>/add_servicing/', views.add_servicing, name='add_servicing'),
 path('autos/<int:auto_id>/add_photo/', views.add_photo, name='add_photo'),

 path('autos/<int:auto_id>/assoc_show/<int:show_id>/', views.assoc_show, name='assoc_show'),
 path('autos/<int:auto_id>/unassoc_show/<int:show_id>/', views.unassoc_show, name='unassoc_show'),
 path('shows/', views.ShowList.as_view(), name='shows_index'),
 path('shows/<int:pk>/', views.ShowDetail.as_view(), name='shows_detail'),
 path('shows/create/', views.ShowCreate.as_view(), name='shows_create'),
 path('shows/<int:pk>/update/', views.ShowUpdate.as_view(), name='shows_update'),
 path('shows/<int:pk>/delete/', views.ShowDelete.as_view(), name='shows_delete'),
 path('accounts/', include('django.contrib.auth.urls')),
 path('accounts/signup', views.signup, name='signup'),
]