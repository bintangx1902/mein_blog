from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views.generic import *
from .forms import *
from .utils import staff_required, slug_generator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404


link = 'link'


class AdminHome(ListView):
    template_name = "be/home.html"
    model = Post
    context_object_name = 'post'
    paginate_by = 10
    ordering = ['-id']

    @method_decorator(login_required(login_url='/admin/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminHome, self).dispatch(request, *args, **kwargs)


class CreatePost(CreateView):
    template_name = "be/create.html"
    model = Post
    form_class = CreatePostForm

    def get_success_url(self):
        return reverse('my:home')

    def form_valid(self, form):
        get_link = form.cleaned_data['title']
        slug_ = get_link.replace(' ', '-')
        form.instance.link = slug_
        return super(CreatePost, self).form_valid(form)

    @method_decorator(login_required(login_url='/admin/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(CreatePost, self).dispatch(request, *args, **kwargs)


class UpdatePost(UpdateView):
    template_name = 'be/update.html'
    model = Post
    form_class = CreatePostForm
    query_pk_and_slug = True
    slug_field = link
    slug_url_kwarg = link

    def get_success_url(self):
        return reverse('my:home')

    @method_decorator(login_required(login_url='/admin/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(UpdatePost, self).dispatch(request, *args, **kwargs)


class DeletePost(DeleteView):
    model = Post
    template_name = "be/delete.html"
    query_pk_and_slug = True
    slug_field = link
    slug_url_kwarg = link

    def get_success_url(self):
        return reverse('my:home')

    @method_decorator(login_required(login_url='/admin/login'))
    def dispatch(self, request, *args, **kwargs):
        return super(DeletePost, self).dispatch(request, *args, **kwargs)


class MediaManagerView(ListView):
    model = MediaManager
    paginate_by = 10
    template_name = 'be/media.html'
    ordering = ['-id']
    context_object_name = 'media'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MediaManagerView, self).get_context_data(**kwargs)
        return context

    @method_decorator(login_required(login_url='/admin/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(MediaManagerView, self).dispatch(request, *args, **kwargs)


class MediaUpload(CreateView):
    model = MediaManager
    template_name = 'be/media_upload.html'
    fields = "__all__"

    def get_success_url(self):
        return reverse('my:media-manager')

    def form_valid(self, form):
        form.save(commit=False)
        if self.request.FILES:
            files = self.request.FILES.getlist('file')[:-1]
            for f in files:
                self.model.objects.create(file=f)

        return super().form_valid(form)

    @method_decorator(login_required(login_url='/admin/login/'))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.FILES.getlist('file'):
            return redirect('my:media-manager')
        return super(MediaUpload, self).dispatch(request, *args, **kwargs)


def MediaUploadTest(request):
    if request.method == 'POST':
        files = request.FILES.getlist('file')
        for file in files:
            print(file)

    return redirect('my:media-manager')


def delete_all_media(request):
    media = MediaManager.objects.all()
    if request.method == 'POST':
        for file in media:
            file.delete()

    return redirect("my:media-manager")


def delete_media(request, pk):
    try:
        to_delete = get_object_or_404(MediaManager, pk=pk)
    except MediaManager.DoesNotExist:
        return Http404

    if request.method == 'POST':
        to_delete.delete()

    return redirect('my:media-manager')

