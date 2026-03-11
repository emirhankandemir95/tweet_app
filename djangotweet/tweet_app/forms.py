from django import forms

class AddTweetForm(forms.Form):
    username_input = forms.CharField(label="Username",max_length=50)
    message_input = forms.CharField(label="Message",max_length=100)