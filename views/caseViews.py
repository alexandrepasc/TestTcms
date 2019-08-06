import pytz
import uuid
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from common.utils import get_datetime, get_time_stamp
from forms.caseForms import DetailForm, NewForm, SearchForm
from mgrtests.models import TestCase, TestSuite, TestSuitesCases


@login_required
def case(request):
    items = TestCase.objects.all().order_by('name')

    setattr(request, 'view', 'case')
    setattr(request, 'title', 'Cases')

    if request.method == 'POST':
        form = SearchForm(
            initial={
                'name': request.POST.get('name'),
                'created_by': request.POST.get('created_by'),
                'suites': request.POST.get('suites'),
                'suite_select': request.POST.get('suites'),
                'product': request.POST.get('product'),
                'component': request.POST.get('component'),
                'tag': request.POST.get('tag')
            }
        )

        if request.POST.get('suites') != '':
            search_suite = list(TestSuitesCases.objects.filter(
                suite=request.POST.get('suites')
            ).values('case'))

            case_list = []

            for cenas in search_suite:
                case_list.append(str(cenas.get('case')))

            print(case_list)

        else:
            case_list = ''

        search = TestCase.objects.filter(
            name__icontains=request.POST.get('name'),
            created_by__username__icontains=request.POST.get('created_by'),
            **filters('product__id', request.POST.get('product')),
            **filters('component__id', request.POST.get('component')),
            **filters('tag__id', request.POST.get('tag')),
        ).order_by('name')

        if case_list != '':
            search_ = search.filter(id__in=case_list)
            search = search_

        return render(request, 'testMgr/case.html', {'items': search, 'form': form})

    else:
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

            if request.POST.get('suites') != '':
                suite = TestSuite.objects.get(id=request.POST.get('suites'))

                suite_case = TestSuitesCases(pk=uuid.uuid4(), case=item, suite=suite)
                suite_case.save()

            return redirect('/case/')

    else:
        form = NewForm()

    return render(request, 'testMgr/newCase.html', {'form': form})


@login_required
def detail_case(request, pk):
    item = get_object_or_404(TestCase, id=pk)

    setattr(request, 'view', 'case')
    setattr(request, 'title', 'Cases')

    suites_cases = list(TestSuitesCases.objects.filter(case=item.id).values('suite'))
    if len(suites_cases) > 0:
        print(str(suites_cases[0].get('suite')))
        suite = str(suites_cases[0].get('suite'))
    else:
        suite = ''

    print(item.actions)
    actions = item.actions[2:-2].split('\', \'')
    print(actions[0])

    form = DetailForm(
        initial={
            'name': item.name,
            'description': item.description,
            'suite_select': suite,
            'product': item.product,
            'component': item.component,
            'tag': item.tag,
            'notes': item.notes,
            'actions': actions,
        }
    )

    form.fields['suites'].widget.attrs['disabled'] = True
    form.fields['product'].widget.attrs['disabled'] = True
    form.fields['component'].widget.attrs['disabled'] = True
    form.fields['tag'].widget.attrs['disabled'] = True
    form.fields['actions'].widget.attrs['choices'] = actions

    return render(request, 'testMgr/detailCase.html', {'item': item, 'form': form})


@login_required
def get_suites(request):
    items = TestSuite.objects.all().order_by('name')

    data = {}
    data['suites'] = []

    data['suites'].append({'id': '', 'name': '---------'})
    for item in items:
        data['suites'].append({'id': str(item.id), 'name': item.name})

    return JsonResponse(data)


def filters(field, var):
    if var != '':
        return {field: var}
    else:
        return {}


def filters_(field, var, id_list):
    if var != '':
        return {field: id_list}
    else:
        return {}
