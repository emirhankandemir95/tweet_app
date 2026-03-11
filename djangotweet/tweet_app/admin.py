from django.contrib import admin
from tweet_app.models import Tweet

# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Message Group", {"fields": ["message"]}),
        ("Username Group", {"fields": ["username"]})
    ]
    #fields = ["message","username"] 


admin.site.register(Tweet, TweetAdmin)