from django.shortcuts import render, get_object_or_404
from django.views.generic import *
from backend.models import Profile, Post
from .forms import *
from django.db.models import Q as __
from django.urls import reverse
from django.http import HttpResponseRedirect

links = 'link'


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
    slug_field = links
    slug_url_kwarg = links

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        form = CreateCommentForm
        comment = Comment.objects.all().order_by('-id')

        context['form'] = form
        context['comment'] = comment
        return context


class AddSubscriber(CreateView):
    model = Subscriber
    form_class = AddSubscriberForm
    template_name = 'beauty/sub.html'


def add_like(request, link):
    post_to_like = get_object_or_404(Post, link=link)
    if post_to_like:
        post_to_like.likes += 1
        post_to_like.save()

    return HttpResponseRedirect(reverse('beauty:detail', args=[link]))


class AddComment(CreateView):
    model = Comment
    form_class = CreateCommentForm
    query_pk_and_slug = True
    slug_field = links
    slug_url_kwarg = links
    template_name = 'beauty/red.html'

    def get_success_url(self):
        return reverse('beauty:detail', kwargs={'link': self.kwargs[links]})

    def form_valid(self, form):
        def current_pk():
            comment = Comment.objects.all().order_by('-id').first()
            if comment is None:
                return 0
            return int(comment.pk)

        if not self.request.POST.get('name'):
            form.instance.name = f"Anonymous{current_pk()}"
        else:
            form.instance.name = self.request.POST.get('name')

        get_link = get_object_or_404(Post, link=self.kwargs[links])
        form.instance.post_id = get_link.pk

        return super().form_valid(form)


