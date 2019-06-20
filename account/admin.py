from django.contrib import admin
from account.models import User, UserProfileInfo, CooperativeInfo

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username', 'email', 'first_name', 'last_name',]
    list_filter = ['username']

#admin.site.register(User)
admin.site.register(UserProfileInfo)
admin.site.register(CooperativeInfo)


