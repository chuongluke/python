from django.conf.urls import url, include

from feelings.groups import  views
urlpatterns = [
    url(r'^create/$', views.CompanyCreate.as_view(), name='company_create')
]