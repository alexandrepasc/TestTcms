import uuid
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from forms.tagForms import DetailForm, EditForm, NewForm
from mgrtests.models import Component


@login_required
def component(request):
    items = Component.objects.all().order_by('name')

    setattr(request, 'view', 'component')
    setattr(request, 'title', 'Components')

    return render(request, 'others/component.html', {'items': items})
