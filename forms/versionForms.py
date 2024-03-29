from django import forms

from mgrtests.models import Version


class NewForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 1, 'placeholder': 'Product version'}),
        max_length=30,
        help_text='ex. 1.1, 1.5b',
        label='Version:'
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Version description'}),
        max_length=100,
        help_text='The max length of the text is 100.',
    )

    class Meta:
        model = Version
        fields = ['name', 'description', 'product']


class DetailForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 1, 'placeholder': 'Product name', 'readonly': True}),
        max_length=30
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Product description', 'readonly': True}),
        max_length=100,
    )

    class Meta:
        model = Version
        fields = ['name', 'description', 'product']


class EditForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 1, 'placeholder': 'Product version'}),
        max_length=30,
        help_text='ex. 1.1, 1.5b',
        label='Version:'
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Version description'}),
        max_length=100,
        help_text='The max length of the text is 100.',
    )

    class Meta:
        model = Version
        fields = ['name', 'description', 'product']
