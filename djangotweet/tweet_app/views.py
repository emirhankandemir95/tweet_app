from django.shortcuts import render, redirect
from . import models
from django.urls import reverse
from tweet_app.forms import AddTweetForm
# Create your views here.

def listtweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_context = {"tweets": all_tweets}
    return render(request,"tweet_app/listtweet.html",context=tweet_context)

def addtweet(request):
    if request.POST:
        username = request.POST["username"]
        message = request.POST["message"]
        models.Tweet.objects.create(username=username, message=message)
        return redirect(reverse('tweet_app:listtweet'))
    else:
        return render(request,"tweet_app/addtweet.html")
    
def addtweetbyform(request):
    if request.POST:
        print(request.POST)
        return redirect(reverse('tweet_app:listtweet'))
    else:
        form = AddTweetForm()
        return render(request,'tweet_app/addtweetbyform.html', context={"form":form})