import datetime

import django.utils.timezone
from django.db.models import QuerySet
from django.utils.timezone import localtime

from datacenter.models import Passcard, Visit
from datacenter.models import Visit
from django.shortcuts import render


def active_passcards_view(request):
    all_passcards = Passcard.objects.filter(is_active=True)
    current_visits = Visit.objects.filter(leaved_at=None)

    for visit in current_visits:
        print(visit.passcard.owner_name)

    context = {
        'active_passcards': all_passcards,  # люди с активными пропусками
    }

    return render(request, 'active_passcards.html', context)
