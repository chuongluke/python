from django.conf.urls import url, include

from .views import company
from .views import family

company_patterns = [
    url(r'^create/$', company.Create.as_view(), name='create'),
    url(r'^edit/(?P<slug>[-\w]+)/$', company.Update.as_view(), name='update'),
    url(r'^(?P<slug>[-\w]+)/$', company.Detail.as_view(), name='detail')
]

families_patterns = [
    url(r'^create/$', family.Create.as_view(), name='create'),
    url(r'^edit/(?P<slug>[-\w]+)/$', family.Update.as_view(), name='update'),
    url(r'^(?P<slug>[-\w]+)/$', family.Detail.as_view(), name='detail')
]

urlpatterns = [
    url(r'^companies/', include(company_patterns, namespace='companies')),
    url(r'^families/', include(families_patterns, namespace='families'))
]
