from django.contrib import admin
from .models import BaseUser

# Base User Class Register in Admin Site
admin.site.register(BaseUser)

admin.site.site_header = "SIH 2022"
