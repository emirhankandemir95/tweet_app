from django.shortcuts import render, redirect
from . import models
from django.urls import reverse, reverse_lazy
from tweet_app.forms import AddTweetForm, AddTweetModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
# Create your views here.

def listtweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_context = {"tweets": all_tweets}
    return render(request,"tweet_app/listtweet.html",context=tweet_context)

@login_required(login_url="/login")
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
        form = AddTweetForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username_input"]
            message = form.cleaned_data["message_input"]
            models.Tweet.objects.create(username=username, message=message)
            return redirect(reverse('tweet_app:listtweet'))
        else:
            print("error in form!")
    else:
        form = AddTweetForm()
        return render(request,'tweet_app/addtweetbyform.html', context={"form":form})
    
def addtweetbymodelform(request):
    if request.POST:
        form = AddTweetModelForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            message = form.cleaned_data["message"]
            models.Tweet.objects.create(username=username, message=message)
            return redirect(reverse('tweet_app:listtweet'))
        else:
            print("error in form!")
            return render(request,'tweet_app/addtweetbyform.html', context={"form":form})
    else:
        form = AddTweetModelForm()
        return render(request,'tweet_app/addtweetbymodelform.html', context={"form":form})
    
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
