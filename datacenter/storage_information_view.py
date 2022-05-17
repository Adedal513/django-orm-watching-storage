import datetime

import django.utils.timezone
from django.utils.timezone import localtime

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def format_duration(delta: datetime.timedelta) -> str:
    hours, minutes, seconds = str(delta).split('.')[0].split(':')
    string_duration = f'{hours} часов {minutes} минут {seconds} секунд'

    return string_duration


def storage_information_view(request):
    non_closed_visits_info = []
    current_visits_serialized = Visit.objects.all().filter(leaved_at=None)

    for visit in current_visits_serialized:
        visit_info = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': localtime(visit.entered_at),
            'duration': format_duration(visit.get_duration())
        }

        non_closed_visits_info.append(visit_info)

    context = {
        'non_closed_visits': non_closed_visits_info,
    }
    return render(request, 'storage_information.html', context)
