from django.urls import path
from .views import *

app_name = 'beauty'

urlpatterns = [
    path('', MainPage.as_view(), name='home'),
    path('<slug:link>', PostDetail.as_view(), name='detail'),
    path('add-subs', AddSubscriber.as_view(), name='add-subs'),
    path('<slug:link>/like', add_like, name='like'),
    path('<slug:link>/comment', AddComment.as_view(), name='add-comment'),
]
