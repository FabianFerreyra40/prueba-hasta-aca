from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, CategoriaCreateView

app_name = 'apps.posts'

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path("posts/<int:id>/", PostDetailView.as_view(), name='post_individual'),
    path('post/', PostCreateView.as_view(), name='crear_post'),
    path('post/categoria',CategoriaCreateView.as_view(), name='crear_categoria'),

]