from django.shortcuts import render


def home(request):
    setattr(request, 'view', 'home')

    return render(request, 'home.html')


def test_mgr(request):
    setattr(request, 'view', 'testMgr')

    return render(request, 'testMgr.html')


def test_run(request):
    setattr(request, 'view', 'testRun')

    return render(request, 'testRun.html')
