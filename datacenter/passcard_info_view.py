from django.utils import timezone
from django.shortcuts import render

from datacenter.storage_information_view import format_duration
from datacenter.models import Passcard, Visit


def passcard_info_view(request, passcode):
    this_passcard_visits = []
    visits = Visit.objects.filter(passcard__passcode=passcode)
    for visit in visits:
        duration = visit.get_duration()
        this_passcard_visits.append(
            {
                "entered_at": str(timezone.localtime(visit.entered_at)), "duration": format_duration(duration),
                "is_strange": visit.is_visit_long()
                }
            )
    passcard = Passcard.objects.filter(passcode=passcode)
    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
        }
    return render(request, "passcard_info.html", context)
