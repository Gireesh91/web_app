from django.contrib import admin
from .models import AndroidApp

@admin.register(AndroidApp)
class AndroidAppAdmin(admin.ModelAdmin):
    list_display = ('name', 'points_earned')
    # Customize other admin options as needed
