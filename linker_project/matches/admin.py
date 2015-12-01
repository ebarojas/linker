from django.contrib import admin
from matches import models

# Register your models here.
admin.site.register(models.Match)
admin.site.register(models.VacantLike)
admin.site.register(models.UnemployedLike)