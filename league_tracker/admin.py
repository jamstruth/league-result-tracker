from django.contrib import admin
from .models import League, Division, Event, Result

admin.site.register(League)
admin.site.register(Division)
admin.site.register(Event)
admin.site.register(Result)
