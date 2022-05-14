from django.contrib import admin
from .models import Marker

class MarkerAdmin(admin.ModelAdmin):
  list_display = ('marker_type', 'address', 'gps', 'created_on',)
  list_filter = ('marker_type', 'address', 'created_on',)
  search_filter = ('gps', 'address', 'marker_type', 'created_on',)

admin.site.register(Marker, MarkerAdmin)

admin.site.site_header="Marker"