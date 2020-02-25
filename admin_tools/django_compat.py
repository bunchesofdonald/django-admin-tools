try:
    # we use django.urls import as version detection as it will fail on django
    # 1.11 and thus we are safe to use # gettext_lazy instead of ugettext_lazy
    # instead.
    from django.urls import reverse
    from django.utils.encoding import force_str
    from django.utils.translation import gettext_lazy as _
except ImportError:
    from django.core.urlresolvers import reverse
    from django.utils.encoding import force_text as force_str
    from django.utils.translation import ugettext_lazy as _


__all__ = ['_', 'reverse', 'force_str']
