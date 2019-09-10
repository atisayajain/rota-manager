from django.contrib import admin
from .models import MEMBER,RGM,Due,Event_Detail


# Register your models here.
admin.site.register(MEMBER)
admin.site.register(RGM)
admin.site.register(Due)
admin.site.register(Event_Detail)
