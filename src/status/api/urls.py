from django.conf.urls import url, include

from .views import ( 
    StatusAPIView,
    StatusAPIDetailView,
)

urlpatterns = [
    url(r'^$', StatusAPIView.as_view()),
    url(r'^(?P<id>\d+)/$', StatusAPIDetailView.as_view()),
]
