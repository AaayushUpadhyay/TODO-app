from django.contrib import admin
from .models import Task
# Register your models here.


class tAdmin(admin.ModelAdmin):
    list_display=('id','title','complete')
    list_display_links=('id','title')
    list_editable=('complete',)



admin.site.register(Task,tAdmin)