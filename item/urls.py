from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
	# path('', views.index, name='index'),
	path('new/', views.new, name='new'),
	path('detail/<int:pk>', views.detail, name='detail'),
]