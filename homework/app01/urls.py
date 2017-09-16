from django.conf.urls import url
from app01 import views
urlpatterns = [
    url(r'^modify', views.modify),
    url(r'^delete', views.delete),
    url(r'^add', views.add),
    url(r'^check_host', views.check_host),
    url(r'^check_service', views.check_service),
    url(r'^service', views.add_service),
]
