from django.contrib import admin
from .models import CarMake, CarModel


# CarModelInline class
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # Number of extra forms to display


# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'car_type', 'year')
    search_fields = ('name', 'car_make__name', 'car_type', 'year')
    list_filter = ('car_make', 'car_type', 'year')


# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    inlines = [CarModelInline]


# Register models here (only once)
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
