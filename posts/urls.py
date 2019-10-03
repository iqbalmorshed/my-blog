from django.urls import path, include
from .views import PostDetail, PostList

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
]
