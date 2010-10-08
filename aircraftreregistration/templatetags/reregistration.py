from django import template
from aircraftreregistration.models import Timeline

register = template.Library()

@register.filter
def expiration(obj):
    t = Timeline.objects.get(issuance_month=obj.month)
    return t.certificate_expiration

@register.filter
def reapplication_start(obj):
    t = Timeline.objects.get(issuance_month=obj.month)
    return t.reapplication_start

@register.filter
def reapplication_end(obj):
    t = Timeline.objects.get(issuance_month=obj.month)
    return t.reapplication_end
