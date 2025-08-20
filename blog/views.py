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