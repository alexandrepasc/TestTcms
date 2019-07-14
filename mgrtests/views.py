import uuid
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render




@login_required
def home(request):
    setattr(request, 'view', 'home')

    return render(request, 'home.html')


@login_required
def test_mgr(request):
    setattr(request, 'view', 'testMgr')

    return render(request, 'testMgr.html')


@login_required
def test_run(request):
    setattr(request, 'view', 'testRun')

    return render(request, 'testRun.html')
