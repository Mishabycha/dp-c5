from django.shortcuts import render
from blog.models import Tweet, Author

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

def tweet(request, pk):
    tweet = Tweet.objects.get(id=pk)
    context = {
        'tweet': tweet,
    }
    return render(
        request, 
        'blog/tweet.html', 
        context=context,
    )

def authors(request, pk):
    author = Author.objects.get(id=pk)
    context = {
        'author': author,
    }
    return render(
        request,
        'blog/authors.html',
        context=context
    )