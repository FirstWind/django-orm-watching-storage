from django.utils import timezone

from datacenter.models import Passcard, Visit
from django.shortcuts import render

from datacenter.storage_information_view import format_duration


def passcard_info_view(request, passcode):
    this_passcard_visits = []
    detail_info = Visit.objects.filter(passcard__passcode=passcode).values()
    for item in detail_info:
        duration = Visit.get_duration(item)
        this_passcard_visits.append(
            {
                "entered_at": str(timezone.localtime(item["entered_at"])), "duration": format_duration(duration),
                "is_strange": Visit.is_visit_long(item)
                }
            )
    passcard = Passcard.objects.filter(passcode=passcode)
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
        }
    return render(request, 'passcard_info.html', context)
