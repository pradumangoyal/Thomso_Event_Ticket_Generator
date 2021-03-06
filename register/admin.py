import csv
import datetime
from django.http import HttpResponse
from django.contrib import admin
from .models import Participant
# Register your models here.

class ParticipantAdmin(admin.ModelAdmin):
    actions = ['export_as_csv']
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format('Ticket_Data_{}_{}'.format(datetime.date.today(), datetime.datetime.now().time()))
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response
    export_as_csv.short_description = "Export Selected"
admin.site.register(Participant, ParticipantAdmin)
