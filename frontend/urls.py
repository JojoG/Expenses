from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.contrib import admin
from frontend.views import loggedInView, HomeView

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^loggedin', loggedInView, name='logged_in'),
	url(r'^.*$',login_required(HomeView.as_view()), name='home'),
)
