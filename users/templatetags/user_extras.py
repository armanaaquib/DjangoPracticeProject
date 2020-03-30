from django import template
import re

register = template.Library()

@register.filter(name="only_mail")
def only_mail(value, mail_type):
  '''
  This returns only given mail type mail
  '''

  actual_mail_type = re.findall(r'@.*\.', value)[0]

  if mail_type in actual_mail_type:
    return value

  return ''
