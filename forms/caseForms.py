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


class NewForm(forms.ModelForm):
    name = forms.CharField(
        max_length=30
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Suite description'}),
        max_length=100,
        help_text='The max length of the text is 100.',
    )

    suites = forms.CharField(
        label='Suites:',
        widget=forms.Select()
    )

    class Meta:
        model = TestCase
        fields = ['name', 'description', 'suites', 'product', 'component', 'tag', 'actions', 'expected', 'notes']
