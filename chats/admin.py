from django.contrib import admin
import chats.models as my_models


@admin.register(my_models.Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = [field.name for field in my_models.Chat._meta.fields] + ['member_list']


@admin.register(my_models.Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = [field.name for field in my_models.Membership._meta.fields]

