from django.shortcuts import render

from datacenter.models import Passcard


def active_passcards_view(request):
    active_passcards = Passcard.objects.filter(is_active=True)
    context = {
        "active_passcards": active_passcards,  # люди с активными пропусками
    }
    return render(request, "active_passcards.html", context)
