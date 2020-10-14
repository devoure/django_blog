from django import template
#from django.template.defaultfilters import stringfilter

register = template.Library()
@register.filter(name = 'article_shorten_body')
#@stringfilter
def article_shorten_tag(bodytext, length):
    if len(bodytext) > length:
        text = "%s ..." %bodytext[1:length]

    else:
        text = bodytext


    return text
