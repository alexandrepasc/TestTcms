import uuid
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from forms.componentForms import NewForm
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
            item.save()

            return redirect('/newComponent/?id=' + str(item.id))

    else:
        form = NewForm()

    return render(request, 'include/newItem.html', {'form': form})
