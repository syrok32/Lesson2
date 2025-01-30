from django import forms
from django.core.exceptions import ValidationError

from .models import Product

Ban_words = [
    'казино', 'криптовалюта', 'крипта', 'биржа',
    'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

# Базовая форма с общей логикой


class BaseProductForm(forms.ModelForm):
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if int(price) < 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for word in Ban_words:
            if word.lower() in name.lower():
                raise ValidationError(f'Запрещено использовать слово "{word}" в названии.')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for word in Ban_words:
            if word.lower() in description.lower():
                raise ValidationError(f'Запрещено использовать слово "{word}" в описании.')
        return description

    def __init__(self, *args, **kwargs):
        super(BaseProductForm, self).__init__(*args, **kwargs)

        # Стилизация полей
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',  # CSS-класс
                'placeholder': f'Введите {field.label.lower()}'  # Подсказка
            })


class ProductFormModerator(BaseProductForm):
    class Meta:
        model = Product
        fields = "__all__"  # Использовать все поля



class ProductForm(BaseProductForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "image", "category", ]  # Укажите нужные поля
