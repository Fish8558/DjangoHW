from django import forms

from catalog.models import Product

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at',)

    def clean_name(self):
        clean_data = self.cleaned_data.get('name')
        for word in FORBIDDEN_WORDS:
            if word in clean_data.lower():
                raise forms.ValidationError(f'Название продукта содержит запрещенное слово')
        return clean_data
