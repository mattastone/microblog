from django.views.generic import ListView, DetailView
from .models import Post

class PublishedPostMixin(object):
    def get_queryset(self):
        return self.model.objects.live()

class PostListView(PublishedPostMixin,ListView):
    model = Post
        
class PostDetailView(PublishedPostMixin, DetailView):
    model = Post