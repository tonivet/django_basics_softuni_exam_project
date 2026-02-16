from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def querystring(context, **kwargs):
    request = context['request']
    query_params = request.GET.copy()

    for key, value in kwargs.items():
        query_params[key] = value

    return query_params.urlencode()
