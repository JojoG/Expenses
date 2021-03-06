from bootstrap.templatetags.bootstrap import render_popup

__author__ = 'jackdreilly'

from django import template
register = template.Library()


@register.inclusion_tag('expenses/household.html')
def render_household(household):
    """
    render html for a household
    in turn calls the render_person method for members
    """
    return dict(household = household)

@register.inclusion_tag('expenses/household_preview.html')
def render_household_pv(household):
    """
    render html for a household preview
    in turn calls the render_person method for members
    """
    return dict(household = household)

@register.inclusion_tag('expenses/person.html')
def render_person(person):
    """
    render html for a single person
    """
    return dict(person = person)

@register.inclusion_tag('expenses/invite.html')
def render_invite(invite):
    """
    render html for a single person
    """
    return dict(invite = invite)



@register.inclusion_tag('expenses/balance_table.html')
def render_balance_table(household):
    """
    render html for balance table for household
    """
    return dict(household = household)

@register.filter
def percentage(decimal):
    return format(decimal, "%")

@register.inclusion_tag('expenses/transaction_create_tag.html')
def render_transaction_create(household):
    return dict(household=household)

@register.inclusion_tag('expenses/household_transaction_create_tag.html')
def render_household_transaction_create(household):
    return dict(household=household)

@register.inclusion_tag('popup.html')
def render_household_popup():
    popup = dict(body="This creates a new household",title="New Household")
    return render_popup(popup, 'right',-40,0)



@register.filter_function
def order_by(queryset, args):
    args = [x.strip() for x in args.split(',')]
    return queryset.order_by(*args)
