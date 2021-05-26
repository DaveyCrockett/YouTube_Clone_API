from . import views
from django.urls import path

app_name = 'comments'
urlpatterns = [
    path('comments/', views.CommentList.as_view()),
]
