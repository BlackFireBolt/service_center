from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.views.generic.list import ListView

from .models import Device, Service, Manufacturer, Type, Category

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

class ManufacturerView(ListView):
    model = Manufacturer
    #template_name = 'main/search_results.html'

    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Manufacturer.objects.filter(Q(title__icontains=query))
        return object_list