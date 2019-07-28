import uuid
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from common.utils import get_datetime, get_time_stamp
from forms.suiteForms import DetailForm, EditForm, NewForm, SearchForm
from mgrtests.models import TestSuite, Version


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

        print('------------')
        print(request.POST.get('product'))
        print('------------')

        search = TestSuite.objects.filter(
            name__icontains=request.POST.get('name'),
            created_by__username__icontains=request.POST.get('created_by'),
            **filters('product__id', request.POST.get('product')),
            **filters('component__id', request.POST.get('component')),
            **filters('tag__id', request.POST.get('tag')),
            #product__id=request.POST.get('product')
            #component=request.POST.get('component'),
            #tag__Tag_id=request.POST.get('tag')
        ).order_by('name')

        return render(request, 'testMgr/suite.html', {'items': search, 'form': form})

    else:
        form = SearchForm()

    return render(request, 'testMgr/suite.html', {'items': items, 'form': form})


# TODO: for now the version should not be a parameter added in the creation, if it should be set for the suite
@login_required
def new_suite(request):
    setattr(request, 'view', 'suite')
    setattr(request, 'title', 'Suites')

    if request.method == 'POST':
        form = NewForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.id = uuid.uuid4()
            item.created_by = request.user
            item.created_at = get_time_stamp()
            item.save()

            # TODO: need to think if it should go to base template or to detail of new item
            return redirect('/suite/')

    else:
        form = NewForm()

    return render(request, 'testMgr/newSuite.html', {'form': form})


@login_required
def detail_suite(request, pk):
    item = get_object_or_404(TestSuite, id=pk)

    setattr(request, 'view', 'suite')
    setattr(request, 'title', 'Suites')

    if item.updated_at is not None:
        updated_at = get_datetime(item.updated_at)
        
    else:
        updated_at = ''

    form = DetailForm(initial={
        'name': item.name,
        'description': item.description,
        'product': item.product,
        'version': item.version,
        'component': item.component,
        'tag': item.tag,
        'created_by': item.created_by,
        'created_at': get_datetime(item.created_at),
        'updated_by': item.updated_by,
        'updated_at': updated_at
    })

    form.fields['product'].widget.attrs['disabled'] = True
    form.fields['version'].widget.attrs['disabled'] = True
    form.fields['component'].widget.attrs['disabled'] = True
    form.fields['tag'].widget.attrs['disabled'] = True
    form.fields['created_at'].widget.attrs['disabled'] = True
    form.fields['updated_at'].widget.attrs['disabled'] = True

    return render(request, 'testMgr/detailSuite.html', {'item': item, 'form': form})


@login_required
def edit_suite(request, pk):
    item = get_object_or_404(TestSuite, id=pk)

    setattr(request, 'view', 'suite')
    setattr(request, 'title', 'Suites')

    identification = item.id

    if request.method == 'POST':
        form = EditForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)

            # TODO: implement this to the others edit
            obj = TestSuite.objects.filter(name=item.name, description=item.description, product=item.product,
                                           version=item.version, component=item.component, tag=item.tag)

            if not obj:
                TestSuite.objects.filter(id=identification).update(
                    name=item.name,
                    description=item.description,
                    product=item.product,
                    version=item.version,
                    component=item.component,
                    tag=item.tag,
                    updated_by=request.user,
                    updated_at=get_time_stamp()
                )

            return redirect('/detailSuite/' + str(identification) + '/')

    else:
        form = EditForm(initial={
            'name': item.name,
            'description': item.description,
            'product': item.product,
            'version': item.version,
            'component': item.component,
            'tag': item.tag
        })

    return render(request, 'testMgr/editSuite.html', {'item': item, 'form': form})


def get_prod_version(request):
    if request.GET.get('id', None) != '':
        pk = request.GET.get('id', None)

        items = Version.objects.filter(product=pk).order_by('-name')

        data = {
            'none': 'none'
        }

        if items.count() > 0:
            data = {}
            data['versions'] = []

            for item in items:
                data['versions'].append({'id': str(item.id), 'name': item.name})
                # print(data['versions'][len(data['versions']) - 1])

    print(data)

    return JsonResponse(data)


def filters(field, var):
    if var != '':
        return {field: var}
    else:
        return {}
