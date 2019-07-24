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

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(SearchForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['name'].required = False
        self.fields['created_by'].required = False
