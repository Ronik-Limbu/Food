from django.contrib import admin
from .models import Contact,Foods
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['name','email','phone','message']

class FoodAdmin(admin.ModelAdmin):
    list_display=['name','price','description','image']
admin.site.register(Foods,FoodAdmin)