from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blogs.models import Blogpost


# Create your views here.
class BlogpostCreateView(CreateView):
    template_name = 'blogs/blogpost_form.html'
    model = Blogpost
    fields = (
        'title',
        'slug',
        'content',
        'preview',
        'publication_sign'
    )
    success_url = reverse_lazy('blogs:blogpost_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogpostListView(ListView):
    # template_name = 'blogs/blogpost_list.html'
    model = Blogpost

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication_sign=True)
        return queryset


class BlogpostDetailView(DetailView):
    template_name = 'blogs/blogpost_detail.html'
    model = Blogpost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object

class BlogpostUpdateView(UpdateView):
    template_name = 'blogs/blogpost_form.html'
    model = Blogpost
    fields = (
        'title',
        'slug',
        'content',
        'preview',
        'publication_sign'
    )
    success_url = reverse_lazy('blogs:blogpost_list')

class BlogpostDeleteView(DeleteView):
    model = Blogpost
    template_name = 'blogs/blogpost_confirm_delete.html'
    success_url = reverse_lazy('blogs:blogpost_list')