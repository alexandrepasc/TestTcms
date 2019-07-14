import uuid
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from forms.tagForms import DetailForm, NewForm
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
