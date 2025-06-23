from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blog_list'),
    path('blog_list/<int:pk>/', BlogPostDetailView.as_view(), name='blog_detail'),
    path('create/', BlogPostCreateView.as_view(), name='blog_create'),
    path('<int:pk>/edit/', BlogPostUpdateView.as_view(), name='blog_edit'),
    path('<int:pk>/delete/', BlogPostDeleteView.as_view(), name='blog_delete'),
]
