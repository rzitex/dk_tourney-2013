from django.conf.urls import patterns, include, url

from django.views.generic import TemplateView

from tournament.views import TournamentListView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name="home.html"), {}, 'home'),
    # url(r'^dk_tourney/', include('dk_tourney.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^tournaments/$', TournamentListView.as_view(), {}, 'tournament_list'),
)
