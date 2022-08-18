from django.contrib import admin

# Register your models here.
from .models import CourtCase
from .models import File

admin.site.register(File)
admin.site.register(CourtCase)
