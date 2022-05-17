import datetime

from django.utils.timezone import localtime

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    this_passcard_visits = Visit.objects.filter(passcard__passcode=passcode)
    this_passcard_visits_serialized = []

    for visit in this_passcard_visits:
        visit_characteristics_for_view = {
            'entered_at': localtime(visit.created_at),
            'duration': visit.get_formatted_duration(),
            'is_strange': visit.is_visit_long()
        }

        this_passcard_visits_serialized.append(visit_characteristics_for_view)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits_serialized
    }
    return render(request, 'passcard_info.html', context)
