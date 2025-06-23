from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blog.models import BlogPost
from blog.forms import BlogPostForm


class BlogListView(ListView):
    model = BlogPost
    queryset = BlogPost.objects.filter(is_published=True).order_by('-created_at')
    paginate_by = 6


class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()
        return obj


class BlogPostCreateView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    success_url = reverse_lazy('blog:blog_list')


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    success_url = reverse_lazy('blog:blog_list')


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog:blog_list')
