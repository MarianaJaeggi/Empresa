from django.contrib import admin
from .models import *

# Register your models here.




class DocenteAdmin(admin.ModelAdmin):
    list_display = (
        'last_name' ,
        'first_name',
        'age' ,
        'course' ,

    )
    search_fields=('last_name' ,'course')
    list_filter = ('last_name' ,'course' )

    
admin.site.register(Docente,DocenteAdmin)



class NoDocenteAdmin(admin.ModelAdmin):
    list_display = (
        'last_name' ,
        'first_name' ,
        'age' ,
        'office' ,

    )
    search_fields=('last_name' ,'office')
    list_filter = ('last_name' ,'office' )






admin.site.register(NoDocente,NoDocenteAdmin)