import uuid
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import NewProductForm
from .models import Product


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


@login_required
def product(request):
    items = Product.objects.all()

    setattr(request, 'view', 'product')

    if request.method == 'POST':
        form = NewProductForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.id = uuid.uuid4()
            item.created_by = request.user
            item.save()

    else:
        form = NewProductForm()

    return render(request, 'product.html', {'items': items, 'form': form})
