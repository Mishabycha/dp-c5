from django.urls import path
import blog.views as blog_views

urlpatterns = [
    path("", blog_views.tweet_list, name="tweet_list")
]