from django.contrib import admin
from .models import (
    Reason,
    Course,
    Subject,
    Teacher,
    Flat_plan,
    Scientific_area,
    Programming_Language,
    Project,
)


class ReasonAdmin(admin.ModelAdmin):
    list_display = ("text", "order")
    search_fields = ("text",)
    list_editable = ("order",)


class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "course_name",
        "course_ects",
        "semesters",
    )
    search_fields = ("course_name","course_ects")
    list_filter = ("semesters", "scientific_area")


class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "year", "semester", "ects")
    search_fields = ("name",)
    list_filter = ("year", "semester", "scientific_area")


class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "resume")
    search_fields = ("name", "resume")


class Flat_planAdmin(admin.ModelAdmin):
    list_display = ("years",)
    filter_horizontal = ("subjects",)


class Scientific_areaAdmin(admin.ModelAdmin):
    list_display = ("program",)
    filter_horizontal = ("teachers",)


class Programming_LanguageAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("description", "repository")
    filter_horizontal = ("programming_languages",)


admin.site.register(Reason, ReasonAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Flat_plan, Flat_planAdmin)
admin.site.register(Scientific_area, Scientific_areaAdmin)
admin.site.register(Programming_Language, Programming_LanguageAdmin)
admin.site.register(Project, ProjectAdmin)
