from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'), 
    path('add-anon-message/<int:pk>/', views.add_anon_message, name='add-anon-message'), 
    path('all-anon-messages/', views.all_anon_messages, name='all-anon-messages')
]