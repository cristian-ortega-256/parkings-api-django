from django.contrib import admin
from .models import Parkings
from .models import Configuration

# Register your models here.

admin.site.register(Parkings)
admin.site.register(Configuration)