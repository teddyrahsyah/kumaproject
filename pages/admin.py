from django.contrib import admin

from .models import (HomepageContent, HomepageImage, 
                    ServicepageContent, ServicepageImage,
                    AboutpageContent, AboutpageImage,
                    JoinpageContent, JoinpageImage)
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

class AboutpageInlineImage(admin.TabularInline):
    model = AboutpageImage
    min_num = 1
    max_num = 1

class AboutpageAdmin(admin.ModelAdmin):
    inlines = [AboutpageInlineImage]

class JoinpageInlineImage(admin.TabularInline):
    model = JoinpageImage
    min_num = 1
    max_num = 1

class JoinpageAdmin(admin.ModelAdmin):
    inlines = [JoinpageInlineImage]

admin.site.register(HomepageContent, HomepageAdmin)
admin.site.register(ServicepageContent, ServicepageAdmin)
admin.site.register(AboutpageContent, AboutpageAdmin)
admin.site.register(JoinpageContent, JoinpageAdmin)
