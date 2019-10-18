from django.contrib import admin
from .models import Hall, BloodGroup, Department, Donor
# Register your models here.

admin.site.register(Hall)
admin.site.register(BloodGroup)
admin.site.register(Department)
admin.site.register(Donor)