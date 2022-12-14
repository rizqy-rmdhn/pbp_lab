from django.shortcuts import render
from .models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# TODO: Create your views here.
def show_mywatchlist_html(request):
    data_mywatchlist = MyWatchList.objects.all()
    watched_count = MyWatchList.objects.filter(watched=1).count()
    not_watched_count = MyWatchList.objects.filter(watched=0).count()
    msg = ""
    if watched_count >= not_watched_count:
          msg = "Selamat, kamu sudah banyak menonton!"
    else:
          msg = "Wah, kamu masih sedikit menonton!"
    context = {
                'list_mywatchlist': data_mywatchlist,
                'name': 'Muhammad Rizqy Ramadhan',
                'student_id' : '2106632182',
                'message':msg
              }
    return render(request, "mywatchlist.html", context)

def show_mywatchlist_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_mywatchlist_json(request):
  data = MyWatchList.objects.all()
  return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_mywatchlist_json_by_id(request, id):
  data = MyWatchList.objects.filter(pk=id)
  return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_mywatchlist_xml_by_id(request, id):
  data = MyWatchList.objects.filter(pk=id)
  return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")