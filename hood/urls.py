from django.urls import path
from . import views
from .views import (PostDetailView,PostCreateView,PostUpdateView)

urlpatterns=[
    path('',views.home,name='hood-home'),
    path('post/new/',PostCreateView.as_view(),name='post-new'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-new'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
]