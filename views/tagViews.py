import uuid
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from forms.tagForms import DetailForm, EditForm, NewForm
from mgrtests.models import Tag


@login_required
def tag(request):
    items = Tag.objects.all().order_by('name')

    setattr(request, 'view', 'tag')
    setattr(request, 'title', 'Tags')

    return render(request, 'others/tag.html', {'items': items})


@login_required
def new_tag(request):
    if request.method == 'POST':
        form = NewForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.id = uuid.uuid4()
            item.created_by = request.user
            item.save()

            return redirect('/newTag/?page=reload')

    else:
        form = NewForm()

    return render(request, 'include/newItem.html', {'form': form})


@login_required
def detail_tag(request, pk):
    item = get_object_or_404(Tag, id=pk)

    form = DetailForm(initial={'name': item.name, 'description': item.description})

    setattr(request, 'context', 'Tag')

    return render(request, 'include/detailItem.html', {'item': item, 'form': form})


@login_required
def edit_tag(request, pk):
    item = get_object_or_404(Tag, id=pk)

    created_by = item.created_by
    created_at = item.created_at
    identification = item.id

    setattr(request, 'parent', 'tag')

    if request.method == 'POST':
        form = EditForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = created_by
            item.created_at = created_at
            item.updated_at = datetime.now()
            item.id = identification
            item.save()

            return redirect('/detailTag/' + str(item.id) + '/?page=reload')

    else:
        form = EditForm(initial={'name': item.name, 'description': item.description})

        return render(request, 'include/editItem.html', {'form': form, 'item': item})
