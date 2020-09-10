from django.contrib import admin
from course.models import Course


# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name_slug', 'desc','sale' ,'name', 'meta_title', 'image_tag', 'is_top']
