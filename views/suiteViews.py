import uuid
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from common.utils import get_datetime, get_time_stamp
from forms.suiteForms import DetailForm, NewForm, SearchForm
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
