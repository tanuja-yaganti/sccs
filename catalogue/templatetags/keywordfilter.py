from django import template
register = template.Library()

@register.filter(name='split')
def split(keywords,key):
	words = keywords.split(key)
	return words