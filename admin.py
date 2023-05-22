from django.contrib import admin

# Register your models here.
from .models import Machine
admin.site.register(Machine)

from .models import Personne
admin.site.register(Personne)