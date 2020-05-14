from django.contrib import admin
from .models import Listing
# Register your models here.

# First- Registered only Listings model after importing it.

# Second- To customize the listings display in admin created
# ListingAdmin extended with admin.ModelAdmin and Added it
# as second arg to admin.site.register.


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',
                    'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published', )
    search_fields = ('title', 'description', 'address',
                     'city', 'state', 'zipcode', 'price')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
