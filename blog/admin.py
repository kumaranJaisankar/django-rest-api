from django.contrib import admin

# Register your models here.
from . import models 
@admin.register(models.Post)
class Admin(admin.ModelAdmin):
    list_display= ('title','id','author','status','slug')
    prepopulated_fields = {'slug':('title',),}

    



admin.site.register(models.Category)