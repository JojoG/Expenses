from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from expenses.models import Person

@login_required
def loggedInView(request):
    """
    after log in, if no person, create
    """
    user = request.user
    if user.person_set.count() < 1:
        Person(user=user, name = 'Anonymous').save()
    return redirect('/profiles/%s' % user.username)


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        cd = super(HomeView,self).get_context_data(**kwargs)
        get_data = self.request.GET
        if get_data.has_key('popup'):
            cd.update(dict(modal = dict(title='Invite Sent', body='Your invitation has been sent to the user you requested', button1='OK')))
        return cd
