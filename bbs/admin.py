from django.contrib import admin
from .models import Customer,Transaction

# Register your models here.


admin.site.register(Customer)
admin.site.register(Transaction)
admin.site.site_header="Admin Page"
admin.site.site_title="Basic Banking System"
admin.site.index_title="Hi-ADMIN Welcome to the Banking System"