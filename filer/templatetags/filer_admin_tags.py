import django
from django.conf import settings
from django.template import Library
from distutils.version import LooseVersion

if "django.contrib.staticfiles" in settings.INSTALLED_APPS:
    from django.contrib.staticfiles.templatetags.staticfiles import static
else:
    static = lambda path: "%s%s" % (settings.STATIC_URL, path)


register = Library()


def filer_actions(context):
    """
    Track the number of times the action field has been rendered on the page,
    so we know which value to use.
    """
    context['action_index'] = context.get('action_index', -1) + 1
    return context
filer_actions = register.inclusion_tag("admin/filer/actions.html", takes_context=True)(filer_actions)


# Shamelessly taken from django-cms
# This will go away when django < 1.4 compatibility will be dropped
if LooseVersion(django.get_version()) < LooseVersion('1.4'):
    ADMIN_ICON_BASE = static("admin/img/admin/")
    ADMIN_CSS_BASE = static("admin/css/")
    ADMIN_JS_BASE = static("admin/js/")
else:
    ADMIN_ICON_BASE = static("admin/img/")
    ADMIN_CSS_BASE = static("admin/css/")
    ADMIN_JS_BASE = static("admin/js/")

@register.simple_tag
def admin_icon_base():
    return ADMIN_ICON_BASE

@register.simple_tag
def admin_css_base():
    return ADMIN_CSS_BASE

@register.simple_tag
def admin_js_base():
    return ADMIN_JS_BASE
