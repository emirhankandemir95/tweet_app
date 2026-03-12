from django.urls import path
from . import views

app_name = "tweet_app"

urlpatterns = [
    path("",views.listtweet,name="listtweet"), #emirkandemir.com/tweetapp/
    path("addtweet/",views.addtweet,name="addtweet"), #emirkandemir.com/tweetapp/addtweet        
    path("addtweetbyform/",views.addtweetbyform,name="addtweetbyform"), #emirkandemir.com/tweetapp/addtweetbyform
    path("addtweetbymodelform/",views.addtweetbymodelform,name="addtweetbymodelform") #emirkandemir.com/tweetapp/addtweetbymodelform    
]