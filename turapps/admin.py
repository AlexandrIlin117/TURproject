from django.contrib import admin
from .models import pereval_added,Users,Coords,Level,Images, PerevalImages
# Register your models here.


admin.site.register(pereval_added)
admin.site.register(Users)
admin.site.register(Coords)
admin.site.register(Level)
admin.site.register(Images)
admin.site.register(PerevalImages)
