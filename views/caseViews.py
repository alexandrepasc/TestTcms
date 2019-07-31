import pytz
import uuid
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from forms.caseForms import SearchForm
from mgrtests.models import TestCase, TestSuite


@login_required
def case(request):
    items = TestCase.objects.all().order_by('name')

    setattr(request, 'view', 'case')
    setattr(request, 'title', 'Cases')

    form = SearchForm()

    return render(request, 'testMgr/case.html', {'items': items, 'form': form})


def get_suites(request):
    items = TestSuite.objects.all().order_by('name')

    data = {}
    data['suites'] = []

    data['suites'].append({'id': '', 'name': '---------'})
    for item in items:
        data['suites'].append({'id': str(item.id), 'name': item.name})

    return JsonResponse(data)
