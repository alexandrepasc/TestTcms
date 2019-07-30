from django import forms

from mgrtests.models import TestCase, TestSuite


class SearchForm(forms.ModelForm):
    name = forms.CharField(
        max_length=30
    )

    created_by = forms.CharField(
        label='Author:'
    )

    class Meta:
        model = TestCase
        fields = ['name', 'created_by', 'product', 'component', 'tag']

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(SearchForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['name'].required = False
        self.fields['created_by'].required = False


# TODO: this select doesn't have the same style as the others
Suites_choice = TestSuite.objects.values_list('id', 'name')


class SearchSuiteForm(forms.ModelForm):
    suites = forms.CharField(
        label='Suites:',
        widget=forms.Select(choices=Suites_choice)
    )

    class Meta:
        model = TestSuite
        fields = ['suites']
