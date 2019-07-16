from django import forms

from mgrtests.models import Component


class NewForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 1, 'placeholder': 'Component name'}),
        max_length=30
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Component description'}),
        max_length=100,
        help_text='The max length of the text is 100.',
    )

    class Meta:
        model = Component
        fields = ['name', 'description']


class DetailForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 1, 'placeholder': 'Component name', 'readonly': True}),
        max_length=30
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Component description', 'readonly': True}),
        max_length=100,
    )

    class Meta:
        model = Component
        fields = ['name', 'description']


class EditForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 1, 'placeholder': 'Component name'}),
        max_length=30,
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Component description'}),
        max_length=100,
        help_text='The max length of the text is 100.',
    )

    class Meta:
        model = Component
        fields = ['name', 'description']
