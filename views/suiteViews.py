import pytz
import uuid
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from forms.suiteForms import SearchForm
from mgrtests.models import TestSuite


@login_required
def suite(request):
    items = TestSuite.objects.all().order_by('name')

    setattr(request, 'view', 'suite')
    setattr(request, 'title', 'Suites')

    if request.method == 'POST':
        form = SearchForm(
            initial={
                'name': request.POST.get('name'),
                'created_by': request.POST.get('created_by'),
                'product': request.POST.get('product'),
                'component': request.POST.get('component'),
                'tag': request.POST.get('tag')
            }
        )

    else:
        form = SearchForm()

    return render(request, 'testMgr/suite.html', {'items': items, 'form': form})
