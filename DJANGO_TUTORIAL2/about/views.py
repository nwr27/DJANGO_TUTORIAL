from django.shortcuts import render

# Create your views here.
def index(request):
  context = {
    'judul':'About',
    'subjudul':'Ini adalah about Kelas Terbuka',
    'banner':'about/img/banner_about.png'
  }
  return render(request, 'index.html', context)