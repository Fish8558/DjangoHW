from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, FeedbackCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name="product_list"),
    path('product/<int:pk>', ProductDetailView.as_view(), name="product_detail"),
    path('contacts/', FeedbackCreateView.as_view(), name="feedback_create"),
]
