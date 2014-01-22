from django.conf.urls import patterns, include, url
from student.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf.urls.defaults import *
from student.forms import LoginForm
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'students.views.home', name='home'),
    # url(r'^students/', include('students.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^$',group_list),
    (r'^group/(?P<group_id>\d+)/$',stud_list),
    # Uncomment the next line to enable the admin:
	(r'^admin/', include(admin.site.urls)),
	(r'^logout/$', logoutview),
	url(r'^registration/$','simplereg.views.registration',{
		'template_name':'registration/registration.html',
		'autologin':True,
		'callback':None

		},name = 'registration'),

	url(r'^login/$','django.contrib.auth.views.login',{
		'authentication_form':LoginForm
		}, name = 'login'),
)
