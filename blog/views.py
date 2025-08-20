from django.shortcuts import render
from blog.models import Tweet

# Create your views here.

def tweet_list(request):
    tweets = Tweet.objects.all()
    context = {
        "tweet_list": tweets,
    }
    return render(
        request,
        "blog/tweet_list.html",
        context=context,
    )

def tweet(request):
    tweet = Tweet()
    context = {
        'tweet': tweet,
        'title': tweet.title,
        "content": tweet.content,
        "published_date": tweet.published_date,
    }
    return render(
        request, 
        'blog/tweet.html', 
        context=context,
    )

def authors(request):
    pass