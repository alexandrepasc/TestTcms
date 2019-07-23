from django import forms

from mgrtests.models import TestSuite


class SearchForm(forms.ModelForm):
    name = forms.Textarea()

    created_by = forms.CharField(
        label='Author:'
    )

    class Meta:
        model = TestSuite
        fields = ['name', 'created_by', 'product', 'component', 'tag']
