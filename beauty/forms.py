from django import forms
from .models import Subscriber, Comment


class AddSubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = '__all__'


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'content']
