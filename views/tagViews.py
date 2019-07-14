import uuid
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from mgrtests.models import Tag


def tag(request):
    items = Tag.objects.all().order_by('name')

    setattr(request, 'view', 'tag')

    return render(request, 'others/tag.html')
