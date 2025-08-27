from django.urls import path
import blog.views as blog_views

urlpatterns = [
    path("tweets/", blog_views.tweet_list, name="tweet_list"),
    path('tweets/<int:pk>', blog_views.tweet, name='tweet'),
    path('authors/<int:pk>', blog_views.authors, name='authors'),
]
