from django.shortcuts import render, get_object_or_404
from django.views.generic import *
from backend.models import Profile, Post
from .forms import *
from django.db.models import Q as __

link = 'link'


# class MainPage(TemplateView):
#     template_name = 'beauty/main.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(MainPage, self).get_context_data(**kwargs)
#         profile = get_object_or_404(Profile, pk=1)
#         post = Post.objects.all()
#
#         context['profile'] = profile
#         context['post'] = post
#         return context


class MainPage(ListView):
    model = Post
    template_name = 'beauty/main.html'
    ordering = '-id'
    paginate_by = 10
    context_object_name = 'post'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is not None:
            return Post.objects.filter(
                __(title__icontains=query) | __(content__icontains=query)
            ).order_by(self.ordering)
        return Post.objects.all().order_by(self.ordering)


class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'beauty/detail.html'
    query_pk_and_slug = True
    slug_field = link
    slug_url_kwarg = link


class AddSubscriber(CreateView):
    model = Subscriber
    form_class = AddSubscriberForm
    template_name = 'beauty/sub.html'
