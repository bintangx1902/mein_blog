from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('', api_preview, name='api'),
    path('post', post_list, name="post"),
    path('post/<slug:link>', post_detail, name='post-detail'),
]
