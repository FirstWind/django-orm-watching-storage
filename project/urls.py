from datacenter.active_passcards_view import active_passcards_view
from datacenter.passcard_info_view import passcard_info_view
from datacenter.storage_information_view import storage_information_view
from django.conf.urls import url


urlpatterns = [
    url(r"^$", active_passcards_view, name="active_passcards"),
    url(r"^storage_information$", storage_information_view, name="storage_information"),
    url(r"^passcard_info/(?P<passcode>[\w\-]+)/$", passcard_info_view, name="passcard_info"),
]
