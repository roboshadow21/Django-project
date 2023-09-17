from django import forms


class ImageForm(forms.Form):
    image = forms.ImageField()


class EditProductForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите название продукта'}))
    prod_id = forms.IntegerField(min_value=1,
                                 widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Введите ID'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control',
                                                               'placeholder': 'Введите цену'}))
