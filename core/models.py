from datetime import datetime

from django.db import models

# Create your models here.

status_choices = (
    ("ACTIVE", "ACTIVE"),
    ("NEGATIVE", "NEGATIVE"),
    ("HAS_SYMPTOMS", "HAS_SYMPTOMS"),
)


class Employee(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    dob = models.DateField()
    current_position = models.CharField(max_length=255)

    objects = models.Manager()

    def __str__(self):
        return self.name


class CovidActivity(models.Model):
    symptoms = models.CharField(max_length=255)
    is_active = models.BooleanField()
    date_started = models.DateTimeField()
    last_updated = models.DateTimeField()
    status = models.CharField(choices=status_choices, max_length=255)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        covid_activty = super(CovidActivity, self).save(force_insert, force_update, using, update_fields)
        new_covid_history = CovidActivityHistory(current_status=self.status, activity_id=self.id)
        CovidActivityHistory.save(new_covid_history)

        return covid_activty


class CovidActivityHistory(models.Model):
    date_changed = models.DateTimeField(default=datetime.now)
    current_status = models.CharField(max_length=255)
    activity = models.ForeignKey(CovidActivity, on_delete=models.CASCADE)
