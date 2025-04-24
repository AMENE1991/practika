from django.contrib import admin

from .models import Property, Booking

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'price_per_night')
    search_fields = ('name', 'address')
    list_filter = ('price_per_night',)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'property', 'check_in_date', 'check_out_date', 'status')
    search_fields = ('user__username', 'property__name')
    list_filter = ('status', 'check_in_date', 'check_out_date')

admin.site.register(Property, PropertyAdmin)
admin.site.register(Booking, BookingAdmin)