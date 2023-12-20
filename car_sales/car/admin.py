from django.contrib import admin
from .models import *
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','slug']

admin.site.register(car)
admin.site.register(buy_record)
admin.site.register(comment)
admin.site.register(brand,CategoryAdmin)
