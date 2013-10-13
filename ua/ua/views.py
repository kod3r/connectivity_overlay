from django.template.loader import get_template
from django.template import Context

from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello World")

def index(request):
    t = get_template('index.html')
    html = t.render(Context({}))
    return HttpResponse(html)


