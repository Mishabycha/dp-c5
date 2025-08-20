from django.urls import path
import blog.views as blog_views

urlpatterns = [
    path("", blog_views.tweet_list, name="tweet_list"),
    path('', blog_views.tweet, name='tweet'),
    #path('', blog_views.authors, name='authors'),
]
