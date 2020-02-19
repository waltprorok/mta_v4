from django.contrib import admin
from cal.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_time', 'end_time')
    list_filter = ('title', 'start_time', 'end_time')
