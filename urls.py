from django.conf.urls.defaults import *
from django.conf import settings

from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^myproject/', include('myproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('3760.cv.views',
    url(r'^index/$', 'index', name='cv-index'),
    url(r'^editcv/$', 'editcv', name='cv-editcv'),
    url(r'^form1/$', 'form1', name='cv-form1'),
    url(r'^executive/$', 'executive', name='cv-executive'),
    url(r'^biographical/$', 'biographical', name='cv-biographical'),
    url(r'^offCampusRecognition/$', 'offCampusRecognition', name='cv-offCampusRecognition'),
    url(r'^ServiceAndAdmin/$', 'ServiceAndAdmin', name='cv-ServiceAndAdmin'),
    url(r'^ReportOnTeaching/$', 'ReportOnTeaching', name='cv-ReportOnTeaching'),
    url(r'^ResearchGrants/$', 'ResearchGrants', name='cv-ResearchGrants'),
    url(r'^Courses/$', 'Courses', name='cv-Courses'),
    url(r'^ResearchActivity/$', 'ResearchActivity', name='cv-ResearchActivity'),
    url(r'^doe/$', 'distribution_of_effort', name='cv-doe'),
)

urlpatterns += patterns('',
    (r'^$', redirect_to, {'url': '/index/'}),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':
        'login.html'}, name="cv-login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page':
        '/login/'}, name="cv-logout")
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
