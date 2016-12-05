from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from focus.upload import upload_image

from focus import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r"^uploads/(?P<path>.*)$",\
	        "django.views.static.serve",\
	        {"document_root":settings.MEDIA_ROOT,}
	    ),
	#url(r"^focus/",include(focus_urls)),
	url(r"^",include("focus.urls")),
	url(r"^admin/upload/(?P<dir_name>[^/]+)$",upload_image,name= "upload_image"),
]
