from django.shortcuts import render


def home(request):

    setattr(request, 'view', 'home')

    return render(request, 'home.html')


def testMgr(request):

    setattr(request, 'view', 'testMgr')

    return render(request, 'testMgr.html')
