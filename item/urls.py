from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
	# path('', views.index, name='index'),
	path('new/', views.new, name='new'),
	path('browse/', views.browse, name='browse'),
	path('edit/<int:pk>/', views.edit, name='edit'),
	path('delete/<int:pk>/', views.delete, name='delete'),
	path('detail/<int:pk>', views.detail, name='detail'),
]