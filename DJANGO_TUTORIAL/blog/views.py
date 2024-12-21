from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  return render(request, 'blog.html')

def recent(request):
  return HttpResponse('ini recent post, kalau hanya ini recent maka yang muncul ini aja (ada apa dengan kata recent di HttpResponse)')