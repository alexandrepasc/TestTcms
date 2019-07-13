import uuid
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from mgrtests.models import Version


@login_required
def version(request):
    items = Version.objects.all().order_by('name')

    setattr(request, 'view', 'product')

    return render(request, 'version/version.html', {'items': items})
