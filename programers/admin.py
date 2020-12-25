from django.contrib import admin
import programers.models as my_models


@admin.register(my_models.SoloProgramer)
class SoloProgramerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in my_models.SoloProgramer._meta.fields] + ['skill_list']


@admin.register(my_models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = [field.name for field in my_models.Team._meta.fields] + ['member_list', 'skill_list']


@admin.register(my_models.Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = [field.name for field in my_models.Membership._meta.fields]


@admin.register(my_models.Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = [field.name for field in my_models.Skill._meta.fields]


@admin.register(my_models.SoloProgSkill)
class SoloProgSkillAdmin(admin.ModelAdmin):
    list_display = [field.name for field in my_models.SoloProgSkill._meta.fields]

# admin.site.register(my_models.TeamSkill)
@admin.register(my_models.TeamSkill)
class TeamSkillAdmin(admin.ModelAdmin):
    list_display = [field.name for field in my_models.TeamSkill._meta.fields]
