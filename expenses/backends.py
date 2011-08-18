__author__ = 'jackdreilly'
from registration.backends.default import DefaultBackend

class ExpensesRegisterBackend(DefaultBackend):

    def register(self, request, **kwargs):
        new_user = super(ExpensesRegisterBackend,self).register(request,**kwargs)
        new_user.first_name = kwargs['first_name']
        new_user.last_name = kwargs['last_name']
        new_user.save()
        return new_user
