from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify
from blog.forms import ArticleForm
from blog.models import Article


class ArticleListView(ListView):
    model = Article
    extra_context = {
        'title': 'Статьи'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class ArticleDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'blog.view_article'
    model = Article
    extra_context = {
        'title': 'Статьи'
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class ArticleCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'blog.add_article'
    model = Article
    form_class = ArticleForm
    extra_context = {
        'title': 'Добавление статьи'
    }

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.owner = self.request.user
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.object.slug])


class ArticleUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'blog.change_article'
    model = Article
    form_class = ArticleForm
    extra_context = {
        'title': 'Редактирование статьи'
    }

    def get_success_url(self):
        return reverse('blog:view', args=[self.object.slug])


class ArticleDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'blog.delete_article'
    model = Article
    extra_context = {
        'title': 'Удаление статьи'
    }

    success_url = reverse_lazy("blog:list")
