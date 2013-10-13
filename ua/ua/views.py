from django.http import HttpResponse

def hello(request):
        return HttpResponse("Hello World")

def index(request):
        return HttpResponse("Oldest Joke in the Book")


