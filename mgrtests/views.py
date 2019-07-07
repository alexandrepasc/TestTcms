from django.shortcuts import redirect, render

from common.utils import isLogin


def home(request):
    if isLogin(request):

        setattr(request, 'view', 'home')

        return render(request, 'home.html')

    else:

        return redirect('/login/?next=/')


def test_mgr(request):
    if isLogin(request):

        setattr(request, 'view', 'testMgr')

        return render(request, 'testMgr.html')

    else:

        return redirect('/login/?next=/TestMgr/')


def test_run(request):
    if isLogin(request):

        setattr(request, 'view', 'testRun')

        return render(request, 'testRun.html')

    else:

        return redirect('/login/?next=/TestRun/')
