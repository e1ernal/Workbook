from ModelsApp.models import *
from django.contrib import admin

@admin.register(Filter)
class FilterAdmin(admin.ModelAdmin):
    pass

@admin.register(Image)
class FilterAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class FilterAdmin(admin.ModelAdmin):
    pass

@admin.register(TaskImage)
class FilterAdmin(admin.ModelAdmin):
    pass