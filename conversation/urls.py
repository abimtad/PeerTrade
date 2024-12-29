from django.urls import path
from . import views

app_name = 'conversation'

urlpatterns = [
	path('new/item/<int:pk>/', views.newChat, name='newChat'),
	path('inbox/', views.inbox, name='inbox'),
	path('detail/<int:pk>/', views.detail, name='detail'),
	
]