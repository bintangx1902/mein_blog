from django import forms
from .models import *


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'keyword', 'desc']

        widgets = {
            'keyword': forms.TextInput(),
            'desc': forms.TextInput()
        }


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
