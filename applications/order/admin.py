from django.contrib import admin

from applications.order.models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ['owner', 'product', 'status', 'amount', 'total_price']

admin.site.register(Order, OrderAdmin)
