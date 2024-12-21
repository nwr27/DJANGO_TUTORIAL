from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  context = {
    'judul':'Kelas Terbuka',
    'subjudul':'faqihza',
  }
  return render(request, 'index.html', context)

def about(request):
  context = {
    'judul':'Kelas Terbuka',
    'subjudul':'nwr27',
  }
  return render(request, 'about.html', context)