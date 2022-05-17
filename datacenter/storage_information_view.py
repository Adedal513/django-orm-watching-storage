import datetime

import django.utils.timezone
from django.utils.timezone import localtime

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    current_visits_serialized = []
    current_visits = Visit.objects.filter(leaved_at=None)

    for visit in current_visits:
        visit_info = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': localtime(visit.entered_at),
            'duration': visit.get_formatted_duration(),
            'is_strange': visit.is_visit_long()
        }

        current_visits_serialized.append(visit_info)

    context = {
        'non_closed_visits': current_visits_serialized,
    }
    return render(request, 'storage_information.html', context)
