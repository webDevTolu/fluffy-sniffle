from django.contrib import admin
from api.models import Project

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    list_filter = ('name', 'created_at', 'updated_at',)


admin.site.register(Project)
