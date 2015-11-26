from django.contrib import admin
from match import models

# Register your models here.
admin.site.register(models.Match)
admin.site.register(models.HeadhunterLike)
admin.site.register(models.UnemployedLike)