from django.contrib import admin
from.models import Aiquest

# Register your models here.
@admin.register(Aiquest)
class AiquestAdmin(admin.ModelAdmin):
    list_display =['id','t_name', 'c_name', 'c_duration','seat']