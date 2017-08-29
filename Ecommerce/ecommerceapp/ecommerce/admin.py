from __future__ import unicode_literals

from django.contrib import admin
from .models import Registration , Product , PProduct


class ItemAdmin(admin.ModelAdmin):
	list_display=['Name' ,'Password']
class ItemAdmin2(admin.ModelAdmin):
	list_display=['Name' ,'Prod' ]
class ItemAdmin3(admin.ModelAdmin):
	list_display=['PName' ,'Price' , 'Item', 'Image']
admin.site.register(Registration , ItemAdmin)
admin.site.register(Product , ItemAdmin2)
admin.site.register(PProduct , ItemAdmin3)