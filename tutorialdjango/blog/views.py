#importação para poder usar as duas classes
#DateilView serve para mostrar um post só
#ListView e para lista os posts
from django.views.generic import DetailView, ListView

from.models import Post
#sub class do ListView
class PostListView(ListView):
    model = Post
#sub class do dateilview
class PostDetailView(DetailView):
    model = Post
