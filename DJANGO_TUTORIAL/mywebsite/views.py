from django.http import HttpResponse

def index(request):
  judul = "<h1>Ini adalah Home</h1>"
  subjudul = "<h2>Selamat datang di website ini</h2>"

  output  = judul + subjudul
  return HttpResponse(output)

def about(request):
  return HttpResponse("<h1>Ini About</h1>")