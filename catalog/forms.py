from django import forms
from .models import  Product
from  django.core.exceptions import ValidationError

Ban_words = [
    'казино', 'криптовалюта', 'крипта', 'биржа',
    'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
]


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = "__all__"


    def clean_price(self):
        price = self.cleaned_data.get('price')
        if int(price) < 0:
            raise ValidationError('Ценна не может быть отрицательная')
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
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите имя'  # Текст подсказки внутри поля
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите описание'  # Текст подсказки внутри поля
        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'выбирите картинку'  # Текст подсказки внутри поля
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Выбирите категорию'  # Текст подсказки внутри поля
        })
        self.fields['price'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите ценну '  # Текст подсказки внутри поля
        })