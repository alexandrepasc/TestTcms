import pytz
import uuid
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from forms.productForms import DetailForm, EditForm, NewForm
from mgrtests.models import Product


@login_required
def product(request):
    items = Product.objects.all().order_by('name')

    setattr(request, 'view', 'product')
    setattr(request, 'title', 'Products')

    return render(request, 'product/product.html', {'items': items})


@login_required
def new_product(request):
    setattr(request, 'view', 'product')

    if request.method == 'POST':
        form = NewForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.id = uuid.uuid4()
            item.created_by = request.user
            item.created_at = int(datetime.now(tz=pytz.utc).timestamp() * 1000)
            item.save()

            return redirect('/newProduct/?id=' + str(item.id))

    else:
        form = NewForm()

    return render(request, 'include/newItem.html', {'form': form})


@login_required
def detail_product(request, pk):
    item = get_object_or_404(Product, id=pk)

    setattr(request, 'context', 'Product')
    setattr(request, 'view', 'product')

    form = DetailForm(initial={'name': item.name, 'description': item.description})

    return render(request, 'include/detailItem.html', {'item': item, 'form': form})


@login_required
def edit_product(request, pk):
    item = get_object_or_404(Product, id=pk)

    identification = item.id

    setattr(request, 'view', 'product')

    if request.method == 'POST':
        form = EditForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            # item.created_by = created_by
            # item.id = identification
            # item.save()

            Product.objects.filter(id=identification).update(
                name=item.name,
                description=item.description,
                updated_by=request.user,
                updated_at=int(datetime.now(tz=pytz.utc).timestamp() * 1000)
            )

            return redirect('/detailProduct/' + str(identification) + '/?id=' + str(identification))

    else:
        form = EditForm(initial={'id': item.id, 'name': item.name, 'description': item.description})

        return render(request, 'include/editItem.html', {'form': form, 'item': item})


@login_required
def delete_product(request, pk):
    item = get_object_or_404(Product, id=pk)

    Product.objects.filter(id=item.id).delete()

    return redirect('/product/')
