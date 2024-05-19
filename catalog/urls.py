from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, FeedbackCreateView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, CategoryListView, CategoryDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name="product_list"),
    path('product/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path('product/create/', never_cache(ProductCreateView.as_view()), name="product_create"),
    path('product/update/<int:pk>', never_cache(ProductUpdateView.as_view()), name="product_update"),
    path('product/delete/<int:pk>', never_cache(ProductDeleteView.as_view()), name="product_delete"),
    path('contacts/', FeedbackCreateView.as_view(), name="feedback_create"),
    path('category/', CategoryListView.as_view(), name='categories'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category_detail')
]
