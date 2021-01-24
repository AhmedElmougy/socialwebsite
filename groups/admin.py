from django.contrib import admin
from groups.models import Group,Membership
# Register your models here.


admin.site.register(Group)
admin.site.register(Membership)