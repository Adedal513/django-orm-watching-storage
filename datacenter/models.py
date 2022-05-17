import datetime

from django.db import models
from django.utils.timezone import localtime


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
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self) -> datetime.timedelta:
        visit_started_at = localtime(self.entered_at)
        visit_ended_at = localtime(self.leaved_at) if self.leaved_at else localtime()

        visit_duration = visit_ended_at - visit_started_at

        return visit_duration

    def get_formatted_duration(self) -> str:
        visit_duration = self.get_duration()
        hours, minutes, seconds = str(visit_duration).split('.')[0].split(':')
        string_duration = f'{hours} часов {minutes} минут {seconds} секунд'

        return string_duration

    def is_visit_long(self, minutes=60) -> bool:
        visit_duration = self.get_duration()

        return visit_duration.total_seconds() >= minutes * 60
