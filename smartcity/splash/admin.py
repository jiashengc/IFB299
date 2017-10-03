from django.contrib import admin
from .models import Location

# Register your models here.

class locationAdmin(admin.ModelAdmin):
	list_display = (
		'name',
		'type',
		'address'
	)

	list_filter = (
		'type',
		'city'
	)

admin.site.register(Location, locationAdmin)