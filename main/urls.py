from django.urls import path
from . import views
from .views import MainListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', MainListView.as_view(), name='site-home'),
    
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),

    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),

    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),

    path('about/', MainListView.as_view(), name='site-about'),

    path('', MainListView.as_view(), name='site-home'),
]
