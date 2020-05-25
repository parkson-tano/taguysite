from django.contrib import admin
from .models import Research,Publication,About
# Register your models here.


class ResearchAdmin(admin.ModelAdmin):
    list_display = ('paperName','paperDescription','paper','date')
    search_fields = ['papername']

class PublicationAdmin(admin.ModelAdmin):
    list_display = ('paperName','paperDescription','paper','date')
    search_fields = ['paperName']
class AboutAdmin(admin.ModelAdmin):
    list_display = ['about']


admin.site.register(About, AboutAdmin)
admin.site.register(Research, ResearchAdmin)
admin.site.register(Publication, PublicationAdmin)