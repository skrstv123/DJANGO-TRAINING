from django.contrib import admin
from djangoapp.models import UserData,posts


# Register your models here.

admin.site.register(UserData)
admin.site.register(posts)
# admin.site.register(following)