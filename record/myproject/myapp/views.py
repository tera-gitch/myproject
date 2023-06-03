# myapp/views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
import csv
import codecs

def input_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/myapp/input/')
    else:
        form = ProductForm()

    return render(request, 'myapp/input_form.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'myapp/product_list.html', {'products': products})

def export_products_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="products.csv"'
    response.write(codecs.BOM_UTF8)

    writer = csv.writer(response)

    exclude_fields = ['ID']  # 除外するフィールド名を指定します

    fields = Product._meta.fields
    field_names = [f.verbose_name for f in fields if f.concrete and f.name not in exclude_fields]
    writer.writerow(field_names)

    products = Product.objects.all().values_list(*[f.name for f in fields if f.concrete and f.name not in exclude_fields])
    for product in products:
        writer.writerow(product)

    return response
