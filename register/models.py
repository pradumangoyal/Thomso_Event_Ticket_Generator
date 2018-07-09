from django.db import models

# Create your models here.

class Participant(models.Model):
    id = models.AutoField(primary_key=True)
    thomso_serial_key = models.CharField("Serial Key/ QR Key", max_length=40, unique=True, blank=True)
    name = models.CharField("Team Name/ Participant Name", max_length=128, blank=False)
    institution = models.CharField("Participant's College", max_length=200, blank=False)
    event = models.CharField("Participant's Event" ,max_length=120, blank=False)

    def __str__(self):
        a = self.thomso_serial_key + '/' + self.name
        return (a)
