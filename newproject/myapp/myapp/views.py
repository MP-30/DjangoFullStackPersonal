from django.http import HttpResponse
import datetime

def about(request):
  return HttpResponse("<h1>This is about page</h1>")

def services(request):
  return HttpResponse("<h1>This is services page only</h1>")