from django import forms

from .models import Product


class NewProductForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.CharField(attrs={'placeholder': 'Product name'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Product description'}),
        max_length=100,
        help_text='The max length of the text is 100.',
    )

    class Meta:
        model = Product
        fields = ['name', 'description']
