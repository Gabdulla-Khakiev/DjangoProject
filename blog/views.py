from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blog.models import Post
from blog.forms import PostForm


class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(is_published=True).order_by('-created_at')
    paginate_by = 6


class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()
        return obj


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:blog_list')


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.object.pk})



class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:blog_list')
