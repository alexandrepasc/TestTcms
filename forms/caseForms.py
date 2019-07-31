from django import forms

from mgrtests.models import TestCase, TestSuite


class SearchForm(forms.ModelForm):
    name = forms.CharField(
        max_length=30
    )

    created_by = forms.CharField(
        label='Author:'
    )

    suites = forms.CharField(
        label='Suites:',
        widget=forms.Select()
    )

    class Meta:
        model = TestCase
        fields = ['name', 'created_by', 'suites', 'product', 'component', 'tag']

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(SearchForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['name'].required = False
        self.fields['created_by'].required = False
