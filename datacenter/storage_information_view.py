from django.utils import timezone

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def format_duration(duration):
    hours = int(duration // 3600)
    minutes = int((duration % 3600) // 60)
    seconds = int(duration % 60)
    return '{}ч {}мин {}сек'.format(hours, minutes, seconds)


def storage_information_view(request):
    inside = Visit.objects.filter(leaved_at__isnull=True).values()

    non_closed_visits = []
    for item in inside:
        owner = Passcard.objects.filter(id=item["passcard_id"]).values()[0]
        duration = Visit.get_duration(item)
        non_closed_visits.append(
            {
                "who_entered": owner["owner_name"], "entered_at": str(timezone.localtime(item["entered_at"])),
                "duration": format_duration(duration)
                }
            )

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
        }
    return render(request, 'storage_information.html', context)
