import datetime

import django.utils.timezone
from django.db.models import QuerySet
from django.utils.timezone import localtime

from datacenter.models import Passcard, Visit
from datacenter.models import Visit
from django.shortcuts import render


def active_passcards_view(request):
    all_active_passcards = Passcard.objects.filter(is_active=True)

    context = {
        'active_passcards': all_active_passcards,
    }

    return render(request, 'active_passcards.html', context)
