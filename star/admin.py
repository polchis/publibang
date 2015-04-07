from django.contrib import admin
from star.models import Concurso, Participa, Lugar, TokenParticipa
# Register your models here.

admin.site.register(Concurso)
admin.site.register(Participa)
admin.site.register(Lugar)
admin.site.register(TokenParticipa)