from django.contrib import admin
from shortner.models import UrlShortner

# Register your models here.

class UrlDetailView(admin.ModelAdmin):
    list_display = ('MainUrl', 'uuid', 'Views','Active_Url','Paid')
    list_filter = ('Paid', 'Active_Url')

    search_fields = ['uuid', 'MainUrl',]

admin.site.register(UrlShortner,UrlDetailView)
admin.site.site_header ="Shubham Singh | CRM"