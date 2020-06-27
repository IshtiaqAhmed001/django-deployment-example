from django import template

register = template.Library()

#another way to register by decorators

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')

#one way to register
# register.filter('cut',cut) #first parameter name of the filter and second parameter is the fucntion that is created above
