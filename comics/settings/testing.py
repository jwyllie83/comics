from comics.settings.dev import *

# Use in-memory Sqlite3 database for testing to reduce startup time
DATABASES = {
    'default': {
        'NAME': None,
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

# Remove cache middleware when running tests, as these cause problems in
# django.contrib.{admin,auth,session} unit tests.
MIDDLEWARE_CLASSES = [i for i in MIDDLEWARE_CLASSES
    if not i.startswith('django.middleware.cache')]

# Use a memory cache backend for django.contrib.sessions.tests tests
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# If South is installed system-wide it tries to write to a log file that is
# only accessible as root
SKIP_SOUTH_TESTS=True
