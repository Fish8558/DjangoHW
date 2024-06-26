from django.urls import path
from django.views.decorators.cache import never_cache

from blog.apps import BlogConfig
from blog.views import ArticleListView, ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', ArticleListView.as_view(), name="list"),
    path('create/', never_cache(ArticleCreateView.as_view()), name="create"),
    path('view/<slug:slug>', ArticleDetailView.as_view(), name="view"),
    path('update/<slug:slug>', never_cache(ArticleUpdateView.as_view()), name="update"),
    path('delete/<slug:slug>', never_cache(ArticleDeleteView.as_view()), name="delete"),
]