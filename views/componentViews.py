import pytz
import uuid
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from forms.componentForms import DetailForm, EditForm, NewForm
from mgrtests.models import Component


@login_required
def component(request):
    items = Component.objects.all().order_by('name')

    setattr(request, 'view', 'component')
    setattr(request, 'title', 'Components')

    return render(request, 'others/component.html', {'items': items})


@login_required
def new_component(request):
    setattr(request, 'view', 'component')

    if request.method == 'POST':
        form = NewForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.id = uuid.uuid4()
            item.created_by = request.user
            item.created_at = int(datetime.now(tz=pytz.utc).timestamp() * 1000)
            item.save()

            return redirect('/newComponent/?id=' + str(item.id))

    else:
        form = NewForm()

    return render(request, 'include/newItem.html', {'form': form})


@login_required
def detail_component(request, pk):
    item = get_object_or_404(Component, id=pk)

    setattr(request, 'context', 'Component')
    setattr(request, 'view', 'component')

    form = DetailForm(initial={'name': item.name, 'description': item.description})

    return render(request, 'include/detailItem.html', {'item': item, 'form': form})


@login_required
def edit_component(request, pk):
    item = get_object_or_404(Component, id=pk)

    identification = item.id

    setattr(request, 'view', 'component')

    if request.method == 'POST':
        form = EditForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            # item.id = identification
            # item.created_by = created_by
            # item.created_at = created_at
            # item.update_by = request.user
            # item.updated_at = datetime.now()
            # item.save()

            Component.objects.filter(id=identification).update(
                name=item.name,
                description=item.description,
                updated_by=request.user,
                updated_at=int(datetime.now(tz=pytz.utc).timestamp() * 1000)
            )

            return redirect('/detailComponent/' + str(identification) + '/?id=' + str(identification))

    else:
        form = EditForm(initial={'name': item.name, 'description': item.description})

        return render(request, 'include/editItem.html', {'form': form, 'item': item})


@login_required
def delete_component(request, pk):
    item = get_object_or_404(Component, id=pk)

    Component.objects.filter(id=item.id).delete()

    return redirect('/component/')
