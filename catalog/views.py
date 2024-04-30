from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product, Contact, Feedback


class ProductListView(ListView):
    model = Product
    extra_context = {
        "title": "Главная"
    }


class ProductDetailView(DetailView):
    model = Product
    extra_context = {
        "title": "Товар"
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['version'] = self.object.version.filter(is_active=True).first()
        return context_data


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    extra_context = {
        "title": "Добавление товара"
    }
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    extra_context = {
        "title": "Редактирование товара"
    }

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    extra_context = {
        "title": "Удаление товара"
    }
    success_url = reverse_lazy('catalog:product_list')


class FeedbackCreateView(CreateView):
    model = Feedback
    fields = ('name', 'phone', 'message',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Контакты"
        context["contact"] = Contact.objects.get(pk=1)
        return context

    success_url = reverse_lazy("catalog:product_list")
