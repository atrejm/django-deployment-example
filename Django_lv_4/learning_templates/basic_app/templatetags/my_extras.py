from django import template

register = template.Library()

def remove_chars(value,arg):
    word = list(value)

    for i in range(len(word)):
        if (i+1)%2 == 0:
            word[i] = arg

    word = ''.join([str(elem) for elem in word])
    return word

register.filter("remove_chars", remove_chars)