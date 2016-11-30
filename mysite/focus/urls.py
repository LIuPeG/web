from django.conf.urls import include,url
from . import views


urlpatterns = [
	url(r"^$",views.index,name="index"),
	url(r"^services/",views.services,name="services"),
	url(r"^clients/",views.clients,name="clients"),
	url(r"^add_user/",views.add_user,name="add_user"),
]
