from django import template

register = template.Library()

@register.filter
def newline_to_paragraph(value):

    paragraphs = value.split('\n')
    wrapped_paragraphs = [f'<p>{p.strip()}</p>' for p in paragraphs if p.strip()]
    return ''.join(wrapped_paragraphs)