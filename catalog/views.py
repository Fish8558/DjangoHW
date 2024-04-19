from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
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


class FeedbackCreateView(CreateView):
    model = Feedback
    fields = ('name', 'phone', 'message',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Контакты"
        context["contact"] = Contact.objects.get(pk=1)
        return context

    success_url = reverse_lazy("catalog:product_list")
