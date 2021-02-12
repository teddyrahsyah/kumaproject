from django.contrib import admin

from .models import HomepageContent, HomepageImage, ServicepageContent, ServicepageImage
# Register your models here.

class HomepageInlineImage(admin.TabularInline):
    '''Tabular Inline View for Homepage'''
    model = HomepageImage
    min_num = 1
    max_num = 1

class HomepageAdmin(admin.ModelAdmin):
    inlines = [HomepageInlineImage]


class ServicepageInlineImage(admin.TabularInline):
    '''Tabular Inline View for Homepage'''
    model = ServicepageImage
    min_num = 1
    max_num = 1

class ServicepageAdmin(admin.ModelAdmin):
    inlines = [ServicepageInlineImage]

admin.site.register(HomepageContent, HomepageAdmin)
admin.site.register(ServicepageContent, ServicepageAdmin)
