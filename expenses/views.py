# Create your views here.
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views.generic.list import ListView
from expenses.forms import HouseholdTransactionForm, HouseholdCreateForm, InviteToHouseholdForm
from expenses.models import Person
from expenses.utils import user_in_household
from models import Household, Transaction, Invited


class HouseholdTransactionsView(ListView):

    context_object_name = "transactions"
    template_name = "expenses/household_transactions.html"

    def get_queryset(self):
        return get_object_or_404(Household, pk = self.kwargs['pk']).transaction_set.order_by('-creation_date')


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(HouseholdTransactionsView, self).get_context_data(**kwargs)
        household = get_object_or_404(Household, pk = self.kwargs['pk'])
        context['household'] = household
        return context

    @method_decorator(user_in_household)
    def dispatch(self, *args, **kwargs):
        return super(HouseholdTransactionsView, self).dispatch(*args, **kwargs)


class HouseholdTransactionCreateView(CreateView):
	form_class = HouseholdTransactionForm
	success_url = '/'
	template_name = 'expenses/household_transaction_form.html'
	
	def get_initial(self):
		initial = super(HouseholdTransactionCreateView,self).get_initial()
		if self.kwargs.has_key('pk'):
			h = get_object_or_404(Household,pk=self.kwargs['pk'])
			initial.update(dict(household = h))
			self.success_url = h.get_absolute_url()
		return initial

class HouseholdTransactionUpdateView(UpdateView):
    form_class = HouseholdTransactionForm
    success_url = '/'
    template_name = 'expenses/transaction_edit.html'
    model = Transaction
    
class InviteToHouseholdCreateView(CreateView):
    form_class = InviteToHouseholdForm
    success_url = '/'
    template_name = 'expenses/invite_to_household_form.html'
    model = Invited

    def get_initial(self):
        initial = super(InviteToHouseholdCreateView,self).get_initial()
        if self.kwargs.has_key('pk'):
            initial.update(dict(inviter=Person.getPersonFromUser(self.request.user),household = get_object_or_404(Household,pk=self.kwargs['pk'])))
        return initial    

class HouseholdCreateView(CreateView):
	form_class = HouseholdCreateForm
	template_name = 'expenses/household_form.html'
	success_url = '/'
	def get_initial(self):
		initial = super(HouseholdCreateView,self).get_initial()
		initial.update(dict(person = Person.getPersonFromUser(self.request.user)))
		return initial

class JoinInviteView(DetailView):
    template_name = 'expenses/expenses_base.html'
    model = Invited

    def get_object(self, queryset=None):
        invite = super(JoinInviteView,self).get_object(queryset)
        invite.invitee.household_set.add(invite.household)
        invite.invitee.save()
        return invite
