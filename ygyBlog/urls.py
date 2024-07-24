from django.urls import path
from ygyBlog import views

app_name = 'ygyBlog'

urlpatterns = [
    # Index/Home page
    path('', views.index, name='index'),

    # Browse all blogs
    path('blog/all', views.blog_all, name='blog_all'),

    path('blog/tags', views.blog_tags, name='blog_tags'),

    path('blog/about', views.blog_about, name='blog_about'),

    path('blog/profile/<int:user_id>', views.blog_profile, name='blog_profile'),

    path('blog/detail/<int:blog_id>', views.blog_detail, name='blog_detail'),

    path('blog/post', views.post_blog, name='post_blog'),

    path('blog/comment/post', views.post_comment, name='post_comment'),

    path('category/<int:category_id>/', views.blog_tag_posts, name='blog_tag_posts'),

    path('search/', views.search, name='search'),
]
