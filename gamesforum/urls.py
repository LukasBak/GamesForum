from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum, name="forum"),
    path('thread', views.thread, name="thread"),
    path('new-thread', views.newThread, name="new-thread"),

]