from django.contrib import admin
import projects.models as my_models

# Register your models here.
@admin.register(my_models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [field.name for field in my_models.Project._meta.fields] + ['required_skills']
