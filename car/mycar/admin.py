from django.contrib import admin
from mycar.models import Car

# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass