from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

from comics.common.feeds import ComicFeed
from comics.sets.feeds import SetFeed

feeds = {
    'c': ComicFeed,
    's': SetFeed,
}

urlpatterns = patterns('',
    # Comic common app
    (r'^', include('comics.common.urls')),

    # Comic sets
    (r'^s/', include('comics.sets.urls')),

    # Feedback app
    (r'^feedback/', include('comics.feedback.urls')),

    # Comic feeds
    url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
        {'feed_dict': feeds}, name='feeds'),

    # Django admin
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root),
)

# Let Django host media if doing local development on runserver
if not settings.ADMIN_MEDIA_PREFIX.startswith('http'):
    urlpatterns += patterns('',
        (r'^media/admin/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.ADMIN_MEDIA_ROOT}),
    )
if not settings.MEDIA_URL.startswith('http'):
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
