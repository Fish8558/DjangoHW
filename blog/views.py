from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

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


class ArticleDetailView(DetailView):
    model = Article
    extra_context = {
        'title': 'Статьи'
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'content', 'image', 'is_published')
    extra_context = {
        'title': 'Добавление статьи'
    }

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.object.slug])


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'content', 'image', 'is_published')
    extra_context = {
        'title': 'Редактирование статьи'
    }

    def get_success_url(self):
        return reverse('blog:view', args=[self.object.slug])


class ArticleDeleteView(DeleteView):
    model = Article
    extra_context = {
        'title': 'Удаление статьи'
    }

    success_url = reverse_lazy("blog:list")
