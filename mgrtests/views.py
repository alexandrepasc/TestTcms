import uuid
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .forms import DetailProductForm, NewProductForm
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

    return render(request, 'product/product.html', {'items': items})


@login_required
def new_product(request):
    # items = Product.objects.all()

    if request.method == 'POST':
        form = NewProductForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.id = uuid.uuid4()
            item.created_by = request.user
            item.save()

            return render(request, 'product/newProductReload.html')

    else:
        form = NewProductForm()

        return render(request, 'product/newProduct.html', {'form': form})


@login_required
def detail_product(request, id):
    item = get_object_or_404(Product, id=id)

    form = DetailProductForm(initial={'name': item.name, 'description': item.description})

    return render(request, 'product/detailProduct.html', {'item': item, 'form': form})
