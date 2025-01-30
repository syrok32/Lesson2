from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from blogs.models import Blog
from .forms import AddPostForm


# Create your views here.
class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = AddPostForm
    success_url = reverse_lazy('blogs:blog_list')


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ["headline", "contents", "image", "verified", "count"]
    success_url = reverse_lazy('blogs:blog_list')

    def get_success_url(self):
        return reverse('blogs:blog_det', args=[self.object.pk])


class BlogDeletelView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'blogs/blogs_confirm_delete.html'
    success_url = reverse_lazy('blogs:blog_list')


class BloglDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = 'blogs/blogs_detail.html'
    context_object_name = '/home/'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count += 1
        self.object.save()
        return self.object


class BloglListView(ListView):
    model = Blog
    template_name = 'blogs/blogs_list.html'

    def get_queryset(self):
        return Blog.objects.filter(verified=True)
