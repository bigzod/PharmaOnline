from django.contrib import admin
from website.models import Medicament, Pharmacie, Agence

# Register your models here.
admin.site.register(Medicament)
admin.site.register(Pharmacie)
admin.site.register(Agence)
