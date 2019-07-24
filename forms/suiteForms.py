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


class NewForm(forms.ModelForm):
    name = forms.Textarea()

    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Suite description'}),
        max_length=100,
        help_text='The max length of the text is 100.',
    )

    class Meta:
        model = TestSuite
        fields = ['name', 'description', 'product', 'version', 'component', 'tag']

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(NewForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['product'].required = False
        self.fields['version'].required = False
        self.fields['component'].required = False
        self.fields['tag'].required = False
