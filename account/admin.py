from django.contrib import admin

# Register your models here.
from django.contrib import admin



from account.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserModelAdmin(BaseUserAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = [ "id","email", "fullname","address","phonenumber","is_subscribed","is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        ("User Credentials", {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["fullname","address","phonenumber","is_subscribed"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "fullname", "address","phonenumber", "password1", "password2","is_subscribed"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email","id","fullname"]
    filter_horizontal = []



admin.site.register(User, UserModelAdmin)


