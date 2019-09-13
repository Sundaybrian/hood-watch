from django.urls import path
from . import views
from .views import PostDetailView

urlpatterns=[
    path('',views.home,name='hood-home'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
]