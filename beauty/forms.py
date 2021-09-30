from django import forms
from .models import Subscriber


class AddSubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = '__all__'
