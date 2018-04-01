from django.contrib import admin
from .models import *

# Register your models here.

# Register your models here.
class MaleAdmin(admin.ModelAdmin):
    list_display = ('id','name','birthday','height','job','location','hobbys', 'is_fulled')

class FemaleAdmin(admin.ModelAdmin):
    list_display = ('id','name','birthday','height','job','location','hobbys')

admin.site.register(Male, MaleAdmin)
admin.site.register(Female, FemaleAdmin)