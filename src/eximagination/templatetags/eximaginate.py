from django import template

from ..utils import obtain_image
from ..settings import (
    MEDIA_ROOT,
    MEDIA_RELATIVE_ROOT,
    EXPIRATION_INTERVAL,
    DEBUG
)

__title__ = 'eximagination.templatetags.eximaginate'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('eximaginate',)

register = template.Library()


class EximaginateNode(template.Node):
    """Node for ``eximaginate`` tag.

    .. code-block: html

        {% eximaginate photo as image %}
        {{ image }}

    Eximagination will automatically add ``ei_width`` and ``ei_height``
    variables to the content - those are the original width and height values
    of the obtained image.
    """
    def __init__(self, source_var, force_update, context_name=None):
        self.source_var = template.Variable(source_var)
        self.force_update = bool(force_update)
        self.context_name = context_name

    def render(self, context):
        # Note that this isn't a global constant because we need to change the
        # value for tests.
        try:
            file_data = obtain_image(
                image_source=self.source_var.resolve(context),
                save_to=MEDIA_ROOT,
                media_url=MEDIA_RELATIVE_ROOT,
                force_update=self.force_update,
                expiration_interval=EXPIRATION_INTERVAL,
                debug=DEBUG
            )
            filename = file_data[0]
            # Original width of the obtained image
            context['ei_width'] = file_data[1]
            # Original height of the obtained image
            context['ei_height'] = file_data[2]
            if self.context_name is None:
                return filename

            # We need to get here so we don't have old values in the context
            # variable.
            context[self.context_name] = filename
        except Exception:
            pass

        return ''


@register.tag
def eximaginate(parser, token):
    """Copy an external image locally.

    To just output the absolute url to the thumbnail::

        {% load eximaginate %}

        <img src="{{ MEDIA_URL }}
           {% eximaginate 'http://www.google.com/intl/en/images/logo.gif' %}">

    To put the the downloaded image URL on the context instead of just
    rendering the relative url, finish the tag with ``as [context_var_name]``:

        {% load eximaginate thumbnail %}

        {% eximaginate 'http://www.google.com/intl/en/images/logo.gif'
           as original %}

        <img src="{% thumbnail original 100x100 %}">

    Eximagination will automatically add "ei_width" and "ei_height" variables
    to the content - those are the original width and height values of the
    obtained image.

    TODO: Implement force_update feature (some extra tokens parsing)
    """
    arguments = token.split_contents()
    # Check to see if we're setting to a context variable.

    if len(arguments) < 1:
        raise template.TemplateSyntaxError(
            "{0} tag requires at least one "
            "argument".format(token.contents.split()[0])
        )

    # Get arguments
    if len(arguments) == 4:
        source_var = arguments[1]
        force_update = False  # At the moment force_update is not implemented
        context_name = arguments[3]
    elif len(arguments) == 2:
        source_var = arguments[1]
        force_update = False  # At the moment force_update is not implemented
        context_name = None
    else:
        raise template.TemplateSyntaxError(
            "{0} wrong number arguments".format(token.contents.split()[0])
        )

    # If the size argument was a correct static format, wrap it in quotes so
    # that it is compiled correctly.
    return EximaginateNode(source_var, force_update, context_name)
