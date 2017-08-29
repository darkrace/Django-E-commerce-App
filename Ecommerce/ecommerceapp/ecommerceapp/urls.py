from django.conf import settings
from django.conf.urls import include , url
from django.conf.urls.static import static
from django.contrib import admin
from ecommerce import views


admin.autodiscover()
STATIC_URL = '/static/images'
urlpatterns = [
	url(r'^$', views.index , name='index'),
	url(r'^index', views.index , name='index'),
	url(r'^Image', views.Image , name='Image'),
	url(r'^Login', views.Login , name='Login'),
	url(r'^Logout', views.Logout , name='Logout'),
	url(r'^about', views.about , name='about'),
	url(r'^UserFormView', views.UserFormView , name='UserFormView'),
	url(r'^contact', views.contact , name='contact'),
	url(r'^mens', views.mens , name='mens'),
	url(r'^single', views.single , name='single'),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)