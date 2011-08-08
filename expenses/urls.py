from django.conf.urls.defaults import patterns, url
from django.contrib import admin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from expenses.models import Person, Household, Transaction
from expenses.utils import user_in_household, user_is_person
from expenses.views import HouseholdTransactionsView


admin.autodiscover()


urlpatterns = patterns('',
                       url(r'^person/(?P<pk>\d+)$',user_is_person(DetailView.as_view(model=Person, context_object_name='person')), name='person'),
                       url(r'^household/(?P<pk>\d+)$',user_in_household(DetailView.as_view(model=Household, context_object_name='household')), name='household'),
                       url(r'^household/create/$',CreateView.as_view(model=Household,success_url="/" ), name='household_create'),
                       url(r'^transaction/create/$',CreateView.as_view(model=Transaction, success_url="/"),name='transaction_create'),
                       url(r'^household/(?P<pk>\d+)/transactions/$', HouseholdTransactionsView.as_view(), name='household_transactions'),
)
