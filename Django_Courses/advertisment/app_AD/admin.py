from django.contrib import admin
from .models import AD

class AD_Admin(admin.ModelAdmin):
    list_display = ['id','image', 'title', 'description', 'price', 'created_date', 'updated_date', 'auction',]
    list_filter = ['auction', 'created_at',]
    actions = ['make_auction_as_false', 'make_auction_as_true']
    
    
    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)
    
    
    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)
        
        
admin.site.register(AD,AD_Admin)