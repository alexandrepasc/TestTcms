import uuid
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from mgrtests.forms import DetailProductForm, EditProductForm, NewProductForm
from mgrtests.models import Product


@login_required
def product(request):
    items = Product.objects.all().order_by('name')

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

            return redirect('/newProduct/?page=reload')

    else:
        form = NewProductForm()

        return render(request, 'include/newItem.html', {'form': form})


@login_required
def detail_product(request, pk):
    item = get_object_or_404(Product, id=pk)

    form = DetailProductForm(initial={'name': item.name, 'description': item.description})

    setattr(request, 'context', 'Product')

    return render(request, 'include/detailItem.html', {'item': item, 'form': form})


@login_required
def edit_product(request, pk):
    item = get_object_or_404(Product, id=pk)
    created = item.created_by
    pk = item.id

    if request.method == 'POST':
        form = EditProductForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = created
            item.id = pk
            item.save()

            return redirect('/detailProduct/' + str(item.id) + '/?page=reload')

    else:
        form = EditProductForm(initial={'id': item.id, 'name': item.name, 'description': item.description})

        return render(request, 'include/editItem.html', {'item': item, 'form': form})
