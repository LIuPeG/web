from django.conf.urls import include,url
from views import *


urlpatterns = [
	url(r"^$",index,name="index"),
	#url(r"^services/",views.services,name="services"),
	#url(r"^clients/",views.clients,name="clients"),
	url(r"logout$",do_logout,name="logout"),
	url(r"login",do_login,name="login"),
	url(r"reg",do_reg,name="reg"),
	url(r"^add_user/",add_user,name="add_user"),
]
