from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.template import TemplateDoesNotExist
from django.template.loader import get_template

from .models import Device, Service, Manufacturer

def index(request):
    categories = Manufacturer.objects.all()
    devices = Device.objects.all()
    services = Service.objects.all()
    context = {'categories': categories, 'devices': devices, 'services': services}
    return render(request, 'main/index.html', context)

def other_page(request, page):
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))