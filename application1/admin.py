from django.contrib import admin

from .models import student


class studentAdmin(admin.ModelAdmin):
    list_display=['sid','sname','marks']
admin.site.register(student,studentAdmin)
