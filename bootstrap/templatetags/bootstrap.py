__author__ = 'jackdreilly'


from django import template
register = template.Library()


@register.inclusion_tag('modal.html')
def render_modal(modal):
    """
    render html for a household
    in turn calls the render_person method for members
    """
    return dict(modal = modal)

@register.inclusion_tag('popup.html')
def render_popup(popup, direction,top,left):
    """
    render html for a household
    in turn calls the render_person method for members
    """
    popup.update(dict(direction=direction,top=top,left=left))
    return dict(popup = popup)


