from django.contrib import admin

from students.models import Course


@admin.register(Course)
class Admin(admin.ModelAdmin):
    pass

