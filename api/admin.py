from django.contrib import admin
from .models import Project

# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'createdAt', 'updatedAt')
    list_filter = ('title', 'createdAt', 'updatedAt',)


# admin.site.register(Project)
