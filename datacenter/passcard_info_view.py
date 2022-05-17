import datetime

from django.utils.timezone import localtime

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def format_duration(delta: datetime.timedelta) -> str:
    hours, minutes, seconds = str(delta).split('.')[0].split(':')
    string_duration = f'{hours} часов {minutes} минут {seconds} секунд'

    return string_duration


def is_visit_long(visit: Visit, minutes=60) -> bool:
    visit_duration = visit.get_duration()

    if visit_duration.total_seconds() >= minutes * 60:
        return True

    return False


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    this_passcard_visits_query = Visit.objects.filter(passcard__passcode=passcode)
    this_passcard_visits = []

    for visit in this_passcard_visits_query:
        visit_info = {
            'entered_at': localtime(visit.created_at),
            'duration': format_duration(visit.get_duration()),
            'is_strange': is_visit_long(visit)
        }

        this_passcard_visits.append(visit_info)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
