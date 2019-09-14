from django.contrib import admin
from .models import *

# Register your models here.

class NeighbourhoodAdmin(admin.ModelAdmin):
    filter_horizontal=('locations',)

admin.site.register(Post)
admin.site.register(Business)
admin.site.register(Occupant)
admin.site.register(NeighbourHood,NeighbourhoodAdmin)
admin.site.register(Location)

