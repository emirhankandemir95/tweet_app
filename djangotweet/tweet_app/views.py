from django.shortcuts import render
from . import models

# Create your views here.
def listtweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_context = {"tweets": all_tweets}
    return render(request,"tweet_app/listtweet.html",context=tweet_context)

def addtweet(request):
    if request.POST:
        print(request.POST["nickname"])
        print(request.POST["message"])
    return render(request,"tweet_app/addtweet.html")