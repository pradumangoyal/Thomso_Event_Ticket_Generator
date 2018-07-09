from django.contrib import admin
from .models import Participant
# Register your models here.

class ParticipantAdmin(admin.ModelAdmin):
    pass
admin.site.register(Participant, ParticipantAdmin)
