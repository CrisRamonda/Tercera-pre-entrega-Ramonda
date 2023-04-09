from django.http import HttpResponse
from django.template import loader, Context


def index(request):
    context = {}
    doc = loader.get_template('static/index.html')
    index = doc.render(context)
    return HttpResponse(index)