import uuid
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from forms.versionForms import DetailForm, EditForm, NewForm
from mgrtests.models import Version


@login_required
def version(request):
    items = Version.objects.all().order_by('name')

    setattr(request, 'view', 'version')

    return render(request, 'product/version.html', {'items': items})


@login_required
def new_version(request):
    setattr(request, 'view', 'version')

    if request.method == 'POST':
        form = NewForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.id = uuid.uuid4()
            item.created_by = request.user
            item.save()

            return redirect('/newVersion/?id=' + str(item.id))

    else:
        form = NewForm()

    return render(request, 'include/newItem.html', {'form': form})


@login_required
def detail_version(request, pk):
    item = get_object_or_404(Version, id=pk)

    setattr(request, 'context', 'Version')
    setattr(request, 'view', 'version')

    form = DetailForm(initial={'name': item.name, 'description': item.description, 'product': item.product})

    form.fields['product'].widget.attrs['disabled'] = True

    return render(request, 'include/detailItem.html', {'item': item, 'form': form})


@login_required
def edit_version(request, pk):
    item = get_object_or_404(Version, id=pk)

    setattr(request, 'view', 'version')

    created_by = item.created_by
    identification = item.id

    if request.method == 'POST':
        form = EditForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.id = identification
            item.created_by = created_by
            item.save()

            return redirect('/detailVersion/' + str(item.id) + '/?id=' + str(item.id))

    else:
        form = EditForm(initial={'name': item.name, 'description': item.description, 'product': item.product})

        return render(request, 'include/editItem.html', {'form': form, 'item': item})


@login_required
def delete_version(request, pk):
    item = get_object_or_404(Version, id=pk)

    Version.objects.filter(id=item.id).delete()

    return redirect('/version/')
