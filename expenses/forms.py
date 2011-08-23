from django import forms
from django.forms.models import ModelForm
from expenses.models import Transaction, Household, Person, Invited
from registration.forms import RegistrationForm

class HouseholdTransactionForm(ModelForm):

    household = forms.ModelChoiceField(widget=forms.HiddenInput(),queryset=Household.objects.all())
    class Meta:
        model = Transaction

    def __init__(self,*args,**kwargs):

        super(HouseholdTransactionForm,self).__init__(*args, **kwargs)
        if kwargs['instance']:
            persons = self.instance.household.persons
        elif self.initial.has_key('household'):
            persons  = self.initial['household'].persons
        else:
            persons = Person.objects.all()
        self.fields['transactor'].queryset = persons

    

class InviteToHouseholdForm(ModelForm):   

    household = forms.ModelChoiceField(widget=forms.HiddenInput(),queryset=Household.objects.all())
    inviter = forms.ModelChoiceField(widget=forms.HiddenInput(),queryset=Person.objects.all())
    invitee = forms.ModelChoiceField(label="Person to Invite",queryset=Person.objects.all())
    
    class Meta:
        model = Invited

    def __init__(self,*args,**kwargs):
        super(InviteToHouseholdForm,self).__init__(*args,**kwargs)
        self.fields['invitee'].queryset = Person.objects.exclude(pk = self.initial['inviter'].pk)


class HouseholdCreateForm(ModelForm):
    class Meta:
        model = Household
        fields = ('name',)
    def save(self, commit=True):
        m = super(HouseholdCreateForm, self).save()
        m.persons.add(self.initial['person'])
        m.save()
        return m

class ProfileUpdateForm(ModelForm):
    first_name = forms.CharField('first name')
    last_name = forms.CharField('last name')
    email = forms.EmailField('e-mail address')
    class Meta:
        model = Person
        fields = ('name',)
    def __init__(self,*args,**kwargs):
        super(ProfileUpdateForm,self).__init__(*args, **kwargs)
        u = self.instance.user
        user_stuff = dict([('email', u.email), ('first_name', u.first_name), ('last_name', u.last_name)])
        self.initial.update(user_stuff)
        
    def save(self, force_insert=False, force_update=False, commit=True):
        m = super(ProfileUpdateForm, self).save(commit=False)
        m.user.first_name = self.cleaned_data['first_name']
        m.user.last_name = self.cleaned_data['last_name']
        m.user.email = self.cleaned_data['email']
        if commit:
            m.save()
            m.user.save()
        return m

class MyRegistrationForm(RegistrationForm):
	first_name = forms.CharField('first name')
	last_name = forms.CharField('first name')

	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)
		self.fields.keyOrder = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
