from django import forms
from django.forms import BooleanField

from catalog.models import Product, Version

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at',)

    def clean_name(self):
        clean_data = self.cleaned_data.get('name')
        for word in FORBIDDEN_WORDS:
            if word in clean_data.lower():
                raise forms.ValidationError('Название продукта содержит запрещенное слово')
        return clean_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def clean_version_name(self):
        clean_data = self.cleaned_data.get('version_name')
        for word in FORBIDDEN_WORDS:
            if word in clean_data.lower():
                raise forms.ValidationError('Название версии содержит запрещенное слово')
        return clean_data
