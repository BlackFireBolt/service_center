from django.contrib import admin

from .models import Type, Manufacturer, Device, Service
from .forms import ManufacturerForm


class ManufacturerInline(admin.TabularInline):
    model = Manufacturer


class TypeAdmin(admin.ModelAdmin):
    exclude = ('super_category',)
    inlines = (ManufacturerInline,)


admin.site.register(Type, TypeAdmin)


class ManufacturerAdmin(admin.ModelAdmin):
    form = ManufacturerForm


admin.site.register(Manufacturer, ManufacturerAdmin)


class ServiceInline(admin.TabularInline):
    model = Service


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    fields = ('name', 'category', 'image')
    inlines = (ServiceInline,)


admin.site.register(Device, DeviceAdmin)


admin.site.site_header = 'FMD.BY'