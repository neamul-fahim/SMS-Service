from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('webhook/', views.WebhookView.as_view(), name='webhook'),
    path('chat-window/<str:number>/',
         views.ChatWindowView.as_view(), name='chat_window'),
    path('message/<str:number>/',
         views.MessageView.as_view(), name='message'),
    path('edit-homepage-design/',
         views.MessageView.as_view(), name='edit_homepage_design'),

]
