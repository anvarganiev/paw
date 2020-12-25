from django.contrib import admin
import customers.models as my_models


@admin.register(my_models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in my_models.Customer._meta.fields]


@admin.register(my_models.CustomerSkill)
class CustomerSkillAdmin(admin.ModelAdmin):
    list_display = [field.name for field in my_models.CustomerSkill._meta.fields]

