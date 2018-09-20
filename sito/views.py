# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Page under construction<a href='/sito/about/'>About</a>")

def about(request):
    return HttpResponse("This is the about page <a href='/sito/'>Index</a>")

