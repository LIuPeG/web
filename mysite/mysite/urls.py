from django.conf.urls import include, url
from django.contrib import admin

from focus import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	#url(r"^focus/",include(focus_urls)),
	url(r"^",include("focus.urls")),
]