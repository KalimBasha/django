#a file to create and register user-defined filters

from django import template
register=template.Library()

def swap(value):    #all userdefined filters take one argument that is data or value
    return value.swapcase()

@register.filter('splitting')   #another method to convert normal function to userdefined filters
def split(value,arg):
    return value.split(arg)

@register.filter() 
def length(value):
    return (value,len(value))

@register.filter() 
def count(value,arg):
    return (arg,value.count(arg))

@register.filter() 
def isalpha(value):
    return value.isalpha()

@register.filter() 
def splice(value,d):
    print(d.split(','))
    sv,ev,step=map(int,d.split(','))
    return value[sv:ev:step]

#register.filter('name of filter',function address)   syntax to convert normal function into userdefined filters
register.filter('swapping',swap)