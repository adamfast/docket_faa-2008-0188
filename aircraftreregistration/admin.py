from django.contrib import admin
from models import *

class TimelineAdmin(admin.ModelAdmin):
    list_display = ('issuance_month', 'certificate_expiration', 'reapplication_start', 'reapplication_end')

admin.site.register(Timeline, TimelineAdmin)
