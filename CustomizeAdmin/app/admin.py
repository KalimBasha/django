from django.contrib import admin

# Register your models here.
from app.models import *

class WebpageView(admin.ModelAdmin):
    list_display=['topic_name','name']
    # list_display_links=['url']
    list_editable=('name',)
    list_per_page=1
    search_fields=['name','topic_name']
    list_filter=['name','topic_name']

admin.site.register(Topic)
admin.site.register(Webpage,WebpageView)
admin.site.register(AccessRecord)