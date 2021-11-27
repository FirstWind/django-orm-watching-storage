from django.shortcuts import render
from django.utils import timezone

from datacenter.models import Passcard, Visit


def format_duration(duration):
    hours = int(duration // 3600)
    minutes = int((duration % 3600) // 60)
    seconds = int(duration % 60)
    return "{}ч {}мин {}сек".format(hours, minutes, seconds)


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at__isnull=True)

    non_closed_visits = []
    for visit in visits:
        duration = visit.get_duration()
        owner = Passcard.objects.filter(id=visit.passcard_id)
        if visit.is_visit_long():
            is_strange = "Да!"
        else:
            is_strange = "Нет"
        non_closed_visits.append(
            {
                "who_entered": owner[0].owner_name, "entered_at": str(timezone.localtime(visit.entered_at)),
                "duration": format_duration(duration), "is_strange": is_strange,
                }
            )

    context = {
        "non_closed_visits": non_closed_visits,
        }
    return render(request, "storage_information.html", context)
