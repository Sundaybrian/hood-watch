from django.urls import path
from . import views
from .views import (
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView,
                    BusinessCreateView,
                    BusinessUpdateView,
                    UserBusinessListView,
                    BusinessDetailView
)

urlpatterns=[
    path('',views.home,name='hood-home'),
    path('post/new/',PostCreateView.as_view(),name='post-new'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-new'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('user/<str:username>/posts/',UserPostListView.as_view(),name='user-posts'),
    path('business/new/',BusinessCreateView.as_view(),name='business-new'),
    path('business/<int:pk>/',BusinessDetailView.as_view(),name='business-detail'),
    path('business/<int:pk>/update/',BusinessUpdateView.as_view(),name='business-new'),
    path('user/<str:username>/biznesses/',UserBusinessListView.as_view(),name='user-biz'),
    path('business/neighbourhood/',views.business,name='hood-business')
]
