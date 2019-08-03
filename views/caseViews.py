import pytz
import uuid
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from common.utils import get_datetime, get_time_stamp
from forms.caseForms import NewForm, SearchForm
from mgrtests.models import TestCase, TestSuite


@login_required
def case(request):
    items = TestCase.objects.all().order_by('name')

    setattr(request, 'view', 'case')
    setattr(request, 'title', 'Cases')

    form = SearchForm()

    return render(request, 'testMgr/case.html', {'items': items, 'form': form})


@login_required
def new_case(request):
    setattr(request, 'view', 'case')
    setattr(request, 'title', 'Cases')

    if request.method == 'POST':
        form = NewForm(request.POST)

        print(request.POST.get('actions'))
        if request.POST.get('actions') != '':
            aux_actions = request.POST.get('actions')[:-1].split('£,')
            aux_expected = request.POST.get('expected')[:-1].split('£,')

        if form.is_valid():
            item = form.save(commit=False)
            item.id = uuid.uuid4()
            item.created_by = request.user
            item.created_at = get_time_stamp()

            if request.POST.get('notes') == '':
                item.notes = None

            if request.POST.get('actions') != '':
                item.actions = aux_actions
                item.expected = aux_expected
            else:
                item.actions = None
                item.expected = None

            item.save()

            return redirect('/case/')

    else:
        form = NewForm()

    return render(request, 'testMgr/newCase.html', {'form': form})


@login_required
def get_suites(request):
    items = TestSuite.objects.all().order_by('name')

    data = {}
    data['suites'] = []

    data['suites'].append({'id': '', 'name': '---------'})
    for item in items:
        data['suites'].append({'id': str(item.id), 'name': item.name})

    return JsonResponse(data)
