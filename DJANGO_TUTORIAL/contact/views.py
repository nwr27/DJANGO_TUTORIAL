from django.shortcuts import render

# Create your views here.
def index(request):
  context = {
    'judul':'Kelas Terbuka',
    'subjudul':'troppo99',
  }
  return render(request, "contact.html", context)