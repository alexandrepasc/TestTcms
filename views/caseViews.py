import pytz
import uuid
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from forms.caseForms import SearchForm, SearchSuiteForm
from mgrtests.models import TestCase


@login_required
def case(request):
    items = TestCase.objects.all().order_by('name')

    setattr(request, 'view', 'case')
    setattr(request, 'title', 'Cases')

    form = SearchForm()
    form_suite = SearchSuiteForm()

    return render(request, 'testMgr/case.html', {'items': items, 'form': form, 'form_suite': form_suite})
