from django.db import models
from django.utils import timezone


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= 'leaved at ' + str(self.leaved_at) if self.leaved_at else 'not leaved'
        )

    def get_duration(visit):
        entered_at = visit["entered_at"]
        leaved_at = visit["leaved_at"]
        if visit["leaved_at"]:
            delta = leaved_at - entered_at
        else:
            delta = timezone.now() - entered_at
        seconds = delta.total_seconds()
        return seconds

    def is_visit_long(visit, minutes=60):
        if Visit.get_duration(visit) // 60 > minutes:
            return True
        return False