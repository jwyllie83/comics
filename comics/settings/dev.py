from comics.settings.base import *
try:
    from comics.settings.local import *
except ImportError:
    pass

DEBUG = True
TEMPLATE_DEBUG = DEBUG

try:
    import debug_toolbar
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INSTALLED_APPS += ('debug_toolbar',)
except ImportError:
    pass

try:
    import django_extensions
    INSTALLED_APPS += ('django_extensions',)
except ImportError:
    pass
