from django.conf.urls import url, include

from ..views import UserDetalAPIView

urlpatterns = [
    url(r'^(?P<username>\w+)/$', UserDetalAPIView.as_view(), name='detail')
]
