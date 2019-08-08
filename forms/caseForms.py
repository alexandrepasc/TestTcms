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
    suite_select = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = TestCase
        fields = ['name', 'created_by', 'suites', 'suite_select', 'product', 'component', 'tag']

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

    notes = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5}),
        max_length=2000,
        help_text='The max length of the text is 2000.',
    )

    actions = forms.CharField(
        max_length=50
    )

    expected = forms.CharField(
        max_length=50
    )

    class Meta:
        model = TestCase
        fields = ['name', 'description', 'suites', 'product', 'component', 'tag', 'actions', 'expected', 'notes']

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(NewForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['suites'].required = False
        self.fields['product'].required = False
        self.fields['component'].required = False
        self.fields['tag'].required = False
        self.fields['notes'].required = False
        self.fields['actions'].required = False
        self.fields['expected'].required = False


class DetailForm(forms.ModelForm):
    # TODO: the text field works should change the others
    name = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': True}),
        max_length=30
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Suite description', 'readonly': True}),
        max_length=100,
        # help_text='The max length of the text is 100.',
    )

    suites = forms.CharField(
        label='Suites:',
        widget=forms.Select()
    )
    suite_select = forms.CharField(widget=forms.HiddenInput(), required=False)

    notes = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'readonly': True}),
        max_length=2000,
        # help_text='The max length of the text is 2000.',
    )

    actions = forms.MultipleChoiceField(widget=forms.HiddenInput(), required=False)
    expected = forms.MultipleChoiceField(widget=forms.HiddenInput(), required=False)

    created_by = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': True}),
        label='Created by:'
    )

    created_at = forms.DateTimeField(label='Created at:')

    updated_by = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': True}),
        label='Updated by:'
    )

    updated_at = forms.DateTimeField(label='Updated at:')

    class Meta:
        model = TestCase
        fields = ['name', 'description', 'suites', 'suite_select', 'product', 'component', 'tag', 'actions', 'expected',
                  'notes', 'created_by', 'created_at', 'updated_by', 'updated_at']


class EditForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(),
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

    suites = forms.CharField(
        label='Suites:',
        widget=forms.Select()
    )
    suite_select = forms.CharField(widget=forms.HiddenInput(), required=False)

    notes = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5}),
        max_length=2000,
        help_text='The max length of the text is 2000.',
    )

    actions = forms.CharField(
        max_length=50
    )

    expected = forms.CharField(
        max_length=50
    )

    class Meta:
        model = TestCase
        fields = ['name', 'description', 'suites', 'suite_select', 'product', 'component', 'tag', 'actions',
                  'expected', 'notes']

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(EditForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['suites'].required = False
        self.fields['product'].required = False
        self.fields['component'].required = False
        self.fields['tag'].required = False
        self.fields['notes'].required = False
        self.fields['actions'].required = False
        self.fields['expected'].required = False
