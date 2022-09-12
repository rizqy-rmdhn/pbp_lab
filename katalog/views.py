from django.shortcuts import render
from .models import CatalogItem

# TODO: Create your views here.
def show_catalog(request):
    data_barang_catalog = CatalogItem.objects.all()
    context = {
                'list_barang': data_barang_catalog,
                'name': 'Muhammad Rizqy Ramadhan',
                'student_id' : '2106632182',
              }
    return render(request, "katalog.html", context)