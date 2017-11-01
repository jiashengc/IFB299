from django.contrib import admin
from .models import Location
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile
from .models import Event
# Register your models here.

# Add admin options for Locations
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name','type','address')
    list_filter = ('type','city')


# Add admin options for Events    
class EventsAdmin(admin.ModelAdmin):
    list_display = ('name','type','address','date_time')
    list_filter = ('type','city')


# class LogAdmin(admin.ModelAdmin):
#
#

admin.site.register(Location, LocationAdmin)
admin.site.register(Event, EventsAdmin)


# Create class to extend admin options for user profile
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


# Create class for new admin profile with extension included 
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

    
# Replace old user admin settings with extended version
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


