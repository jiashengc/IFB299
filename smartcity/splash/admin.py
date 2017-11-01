from django.contrib import admin
from .models import Location
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile
from .models import Event
# Register your models here.


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name','type','address')
    list_filter = ('type','city')


class EventsAdmin(admin.ModelAdmin):
    list_display = ('name','type','address','date_time')
    list_filter = ('type','city')


# class LogAdmin(admin.ModelAdmin):
#
#

admin.site.register(Location, LocationAdmin)
admin.site.register(Event, EventsAdmin)


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


