import uuid
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from mgrtests.forms import DetailVersionForm, EditVersionForm, NewVersionForm
from mgrtests.models import Version


@login_required
def version(request):
    items = Version.objects.all().order_by('name')

    setattr(request, 'view', 'version')

    return render(request, 'product/version.html', {'items': items})


@login_required
def new_version(request):
    if request.method == 'POST':
        form = NewVersionForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.id = uuid.uuid4()
            item.created_by = request.user
            item.save()

            return redirect('/newVersion/?page=reload')

    else:
        form = NewVersionForm()

    return render(request, 'include/newItem.html', {'form': form})


@login_required
def detail_version(request, pk):
    item = get_object_or_404(Version, id=pk)

    form = DetailVersionForm(initial={'name': item.name, 'description': item.description, 'product': item.product})

    form.fields['product'].widget.attrs['disabled'] = True

    setattr(request, 'context', 'Version')

    return render(request, 'include/detailItem.html', {'item': item, 'form': form})


@login_required
def edit_version(request, pk):
    item = get_object_or_404(Version, id=pk)

    created = item.created_by
    identification = item.id

    setattr(request, 'view', 'version')

    if request.method == 'POST':
        form = EditVersionForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = created
            item.id = identification
            item.save()

            return redirect('/detailVersion/' + str(item.id) + '/?page=reload')

    else:
        form = EditVersionForm(initial={'name': item.name, 'description': item.description, 'product': item.product})

        return render(request, 'include/editItem.html', {'form': form})
