from django.contrib import admin
from .models import CSE,ECE,CIVIL,CHEM,MME,MECH

# Register your models here.
admin.site.register(CSE)
admin.site.register(MME)
admin.site.register(ECE)
admin.site.register(MECH)
admin.site.register(CIVIL)
admin.site.register(CHEM)

