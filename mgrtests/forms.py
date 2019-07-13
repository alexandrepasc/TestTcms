from django import forms

from .models import Product


class NewProductForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 1, 'placeholder': 'Product name'}),
        max_length=30
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Product description'}),
        max_length=100,
        help_text='The max length of the text is 100.',
    )

    class Meta:
        model = Product
        fields = ['name', 'description']


class DetailProductForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 1, 'placeholder': 'Product name', 'readonly': True}),
        max_length=30
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Product description', 'readonly': True}),
        max_length=100,
    )

    class Meta:
        model = Product
        fields = ['name', 'description']


class DetailEditProductForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput())

    name = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 1, 'placeholder': 'Product name'}),
        max_length=30
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Product description'}),
        max_length=100,
        help_text='The max length of the text is 100.',
    )

    class Meta:
        model = Product
        fields = ['name', 'description']
