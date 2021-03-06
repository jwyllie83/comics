*******
Changes
*******

This change log is used to track all major changes to *comics* after the first
versioned release.

v1.1.3 (in development)
=======================

**Crawlers**

- New: ``beyondthetree``
- New: ``dresdencodak``
- New: ``extraordinary``
- New: ``gunnerkrigg``
- New: ``icanbarelydraw``. Contributed by Jim Frode Hoff.
- New: ``manlyguys``. Contributed by Jim Frode Hoff.
- New: ``menagea3``
- New: ``sequentialarts``
- New: ``somethingofthatilk``. Contributed by Jim Frode Hoff.
- Update ``eatthattoast`` after site change.
- Update ``extralife`` to be more robust.
- Update ``questionablecontent`` to be more robust.
- Update ``romanticallyapocalyptic`` to be more robust.
- Update ``threewordphrase`` to be more robust.


v1.1.2 (2011-09-18)
===================

A couple of bugfixes easing the transition from 1.0.x to 1.1.x by jwyllie83,
and some new crawlers.

**Bugfixes**

- Updated South requirement to v0.7, which is needed to support the last
  migration introduced by comics v1.1.0.

- If you use WSGI, you can now add a file ``wsgi/local.py`` based off of
  ``wsgi/local.py.template`` to set local settings for WSGI, like the use of
  ``virtualenv`` and debugging settings. This removes the need for changing Git
  tracked files, like ``deploy.wsgi`` for adding e.g. ``virtualenv`` support.

**Crawlers**

- New: ``buttersafe``
- New: ``doghouse``
- New: ``eatthattoast``
- New: ``hejibits``
- New: ``optipess``
- New: ``savagechickens``
- New: ``threewordphrase``
- New: ``timetrabble``
- Update ``pennyarcade`` after site change.


v1.1.1 (2011-08-22)
===================

Some fixes a week after the v1.1 feature release.

**Bugfixes**

- Fix missing whitespaces on about page after HTML minification.
- Add missing CSRF token to feedback form.

**Crawlers**

- Update ``asofterworld`` to work after feed change.


v1.1.0 (2011-08-15)
===================

- New/upgraded requirements:

  - Django 1.3
  - django_compressor
  - cssmin
  - jsmin

- Page speed improvements:

  - CSS and JavaScript is now merged and minified.
  - HTML is minified.
  - Optional Google Analytics code is upgraded to the asynchronous version.
  - All icons have been replaced with sprites to reduce number of elements that
    must be downloaded.

- Slightly refreshed graphical design.

- The "all comics" list at the bottom of the page have been changed from a
  cloud to lists in four columns.

- The optional comic meta data search functionality have been removed.

- Better handling of inactive comics:

  - Add ``active`` flag to comics.
  - Marked no longer published comics as inactive.
  - Inactive comics are no longer loaded by the ``loadmeta``  command unless
    explicitly specified by name or they have been previously loaded. In other
    words, inactive comics will not automatically be included in new
    installations.
  - Inactive comics are no longer included in the top 10 on the front page.
  - Inactive comics are now marked in the comics list on the bottom of all
    pages.
  - Inactive comics are now marked in the comics list page.
  - Inactive comics are now excluded from the set edit form, effectively
    removing them from the set on save.


v1.0.x to v1.1.x migration guide
--------------------------------

Ordered steps for syncronizing your v1.0.x installation with v1.1.0. You
should perform them in order.

**Using virtualenv**

If you choose to use ``virtualenv`` keeping all of comics' dependencies
sandboxed, be sure to activate the environment both in your cronjob and when
manually executing ``manage.py``::

    source <path_to_virtualenv>/bin/activate
    python manage.py getcomics

If you use WSGI, the WSGI file must be modified to support ``virtualenv``. See
:ref:`example-wsgi-file` for how the bundled WSGI file solves this.

**New dependencies**

There are several new dependencies. All of them are listed in the file
``requirements.txt`` and may be installed using ``pip``, optionally inside a
``virtualenv``::

    pip install -r requirements.txt

To avoid compiling dependencies which are not pure Python and thus requires the
installation of various C libraries and Python's development packages, it may
be wise to use your distribution's package manger for some packages, like
``lxml`` and ``PIL``. E.g. on Ubuntu I would install the dependencies like
this::

    sudo apt-get install python-lxml python-imaging
    pip install -r requirements.txt

This way, ``lxml`` and ``PIL`` are installed from APT, and ``pip`` installs the
remaining pure Python dependencies.

**Settings changes**

Database settings now use the new `Django 1.2 format
<https://docs.djangoproject.com/en/dev/releases/1.2/#specifying-databases>`_.
See ``comics/settings/base.py`` for the new default setting and use it as an
example for porting your ``comics/settings/local.py`` settings file.

**Database migration**

A new database field has been added. To migrate your database to work with
v1.1.0, run::

    python manage.py migrate

.. warning ::

    You need South v0.7 or later to perform the database migration.

    comics v1.1.0's ``requirements.txt`` file only require South v0.6 or later.
    This is a bug, and the migration will not work if you're using South
    v0.6.x.

**Static files  collection**

We now use Django's new static files system. After installing you need to
"collect" your static files. See :ref:`collecting-static-files` for how to do
this.


v1.0.8 (2011-08-10)
===================

Just new and updated crawlers.

**Crawlers**

- New: ``mysticrevolution``
- New: ``theidlestate``
- Update ``havet`` to work after feed removal.
- Update ``reveland`` to work after feed removal.
- Update ``thechalkboardmanifesto`` to work after feed change.
- Update ``utensokker`` to work after feed removal.
- Update ``whattheduck`` schedule.


v1.0.7 (2011-07-13)
===================

Just new and updated crawlers.

**Crawlers**

- New: ``fagprat``
- New: ``gregcomic``
- New: ``satw``
- New: ``shortpacked``
- New: ``stickycomics``
- New: ``tehgladiators``
- Update ``betty`` which has moved from comics.com to gocomics.com.
- Update ``bizarro`` which moved to a new site.
- Update ``brandondraws`` which is no longer published.
- Update ``countyoursheep`` after URL changes.
- Update ``darylcagle`` after change from GIF to JPEG.
- Update ``faktafraverden`` which is no longer published.
- Update ``fminus`` which has moved from comics.com to gocomics.com.
- Update ``getfuzzy`` which has moved from comics.com to gocomics.com.
- Update ``lookingforgroup`` after feed change.
- Update ``m`` as it moved from start.no to dagbladet.no.
- Update ``nemibt`` to work after site change.
- Update ``nerfnow`` which crashed when it did not find an image URL.
- Update ``peanuts`` which has moved from comics.com to gocomics.com.
- Update ``pearlsbeforeswine`` which has moved from comics.com to gocomics.com.
- Update ``pondusbt`` after URL changes.
- Update ``rockybt`` to work after site change.
- Update ``romanticallyapocalyptic`` to use web page instead of feed.
- Update ``roseisrose`` which has moved from comics.com to gocomics.com.
- Update ``treadingground`` to not crash if URL is not found.
- Update ``threadingground`` which is no longer published.
- Update ``yehudamoon`` which was broken by addition of new images.
- Update ``zits`` with new feed URL.
- Update generic GoComics.com crawler to also support larger Sunday issues.


v1.0.6 (2011-02-19)
===================

The 1.0.6 release includes two bugfixes, five new crawlers, and many updated
crawlers. Also, most crawler schedules have been updated to make the status
page more useful.

**Bugfixes**

- :class:`comics.aggregator.lxmlparser.LxmlParser` methods now returns an empty
  list if ``allow_multiple`` is :class:`True` and no value is given for
  ``default``. This ensures that using the return value in for loops will not
  fail if no matches are found.

- :meth:`comics.aggregator.crawler.CrawlerBase.get_crawler_release` does no
  longer create empty releases if the ``do_crawl`` method returns false values,
  like empty lists. It previously only stopped processing if ``do_crawl``
  returned :class:`None`.

- Remove ``safe`` filter from title text, and explicitly use ``escape``, even
  though they should be implicitly escaped. Thanks to XKCD #859.

**Crawlers**

- A lot of comic release schedule updates.
- New: ``nerfnow``
- New: ``romanticallyapocalyptic``
- New: ``schlockmercenary``
- New: ``spaceavalanche``
- New: ``treadingground``
- Update ``butternutsquash`` which is no longer published.
- Update ``charliehorse`` which is no longer published.
- Update ``garfield`` to include Sunday editions.
- Update ``hipsterhitler`` to work after feed change.
- Update ``idiotcomics`` which is no longer published.
- Update ``inktank`` which is no longer published.
- Update ``intelsinsides`` which is no longer published.
- Update ``kiwiblitz`` to work after feed change.
- Update ``lifewithrippy`` which is no longer published.
- Update ``pcweenies`` to work after feed change.
- Update ``petpeevy`` which is no longer published.
- Update ``smbc`` to work after feed change.
- Update ``superpoop`` which is no longer published.
- Update ``thegutters`` to use feed instead of broken page parser.
- Update ``threepanelsoul`` to work after feed change.
- Update ``userfriendly`` to support reruns.
- Update ``wulffmorgenthaler`` to work after site change.


v1.0.5 (2010-12-29)
===================

A couple of bugfixes, and new and updated crawlers.

**Bugfixes**

- Do not throw :exc:`ParserError` in :mod:`comics.aggregator.lxmlparser` when
  the XML document is a all-space string.
- Catch :exc:`socket.error` in :mod:`comics.aggregator.downloader`, like we
  already do in :mod:`comics.aggregator.crawler`.

**Crawlers**

- New: ``brandondraws``
- New: ``crookedgremlins``
- New: ``faktafraverden``
- New: ``lunchdb``
- New: ``orneryboy``
- New: ``reveland``
- Update ``foxtrot`` crawler to work after site change.
- Update ``gws`` to work again, and add text parsing.
- Update ``havet`` meta data.
- Update ``lookingforgroup`` to ignore non-comic releases and fetch multiple
  pages released on the same day.
- Update ``magpieluck`` to handle titles without a dash.
- Update ``questionablecontent`` to not check if the page contains the expected
  date, as that make us lose some releases.
- Update ``utensokker`` to use RSS feed.


v1.0.4 (2010-10-23)
===================

Yet another minor release bringing a bug fix, four new and five updated
crawlers.

**Bugfixes**

- Catch :exc:`socket.error` in :meth:`CrawlerBase.get_crawler_release()`.

**Crawlers**

- New: ``hipsterhitler``
- New: ``marriedtothesea``
- New: ``stuffnoonetoldme``
- New: ``utensokker``
- Update ``boxerhockey`` to use feed instead of site.
- Update ``bugcomic`` to not fail if URL is not empty, and to work after source
  site changes.
- Update ``extralife`` to work after source site changes.
- Update ``gunshow`` to work after source site changes.
- Update ``questionablecontent`` to use site instead of feed, since it lacks
  some releases.


v1.0.3 (2010-07-26)
===================

Another minor release bringing 17 new and 11 updated crawlers.

**Bugfixes**

- Make crawlers handle :exc:`httplib.BadStatusLine` exception raised when HTTP
  responses are empty.
- Make crawlers convert :class:`lxml.etree._ElementUnicodeResult` to unicode
  objects before saving to the database, to avoid ``DatabaseError: can't
  adapt`` errors.
- Handle MIME types like ``image/jpeg, image/jpeg`` returned by
  :class:`mimetools.Message.gettype`.
- Use :attr:`Crawler.headers` for image requests, and not just page requests.

**Crawlers**

- New: ``apokalips``
- New: ``axecop`` (fixes GH-8)
- New: ``boxerhockey``
- New: ``bugcomic`` (fixes GH-11)
- New: ``carpediem``
- New: ``crfh``
- New: ``darylcagle``
- New: ``havet`` (fixes GH-7)
- New: ``heltnils``
- New: ``intelsinsides`` (fixes GH-9)
- New: ``misfile`` (fixes GH-3)
- New: ``notinventedhere`` (fixes GH-4)
- New: ``pondusno``
- New: ``radiogaga``
- New: ``scenesfromamultiverse`` (fixes GH-10)
- New: ``sheldon``
- New: ``thegutters``
- Update ``8bittheater`` which is no longer published.
- Update ``brinkerhoff`` which is no longer published.
- Update ``ctrlaltdelete`` to work after source site changes.
- Update ``ctrlaltdeletesillies`` to work after source site changes.
- Update ``dieselsweetiesweb`` to work after source site changes.
- Update ``eon`` with new source site.
- Update ``lunch`` with new source site.
- Update ``sometingpositive`` to get all releases.
- Update ``supereffective`` to work after source site changes.
- Update ``vgcats`` to work after source site changes.
- Update ``yafgc`` to work after source site changes.


v1.0.2 (2010-04-11)
===================

A minor release to get crawler updates out there. Two new cool but partly
immature features are included, as they do not affect existing features or
change database schema.

**Features**

- Add status page which for each comic shows when releases are fetched compared
  to the comic's release schedule. Contributed by Thomas Adamcik.
- Add support for search in comic's title and text fields, using Haystack.
  Contributed by Thomas Adamcik.

**Crawlers**

- New: ``atheistcartoons``
- New: ``petpeevy``
- Update ``evilinc`` to work again.
- Update ``uvod`` to fetch comment too.
- Update ``gunshow`` to fetch multiple images per release.
- Update ``questionablecontent`` to work again.
- Update ``basicinstructions`` to ignore QR Code.
- Update ``partiallyclips`` with new feed URL.
- Update ``somethingpositive`` with new image URL.
- Update ``spikedmath`` to fetch multiple images per release.


v1.0.1 (2010-02-23)
===================

This release features 17 new crawlers and three updated crawlers, most by
*comic*'s new contributor Jim Wyllie. Let's get more of those!

**Features**

- Add links to official sites via redirect page.
- Add :class:`comics.aggregator.crawler.GoComicsComCrawlerBase` for fast
  gocomics.com crawler creation.
- Add ``headers`` argument to :class:`comics.aggregator.lxmlparser.LxmlParser`
  for adding HTTP headers to requests it makes.
- Add time since last release to ``release-list`` and ``comic-list``.

**Crawlers**

- New: ``babyblues``
- New: ``calamitiesofnature``
- New: ``charliehorse``
- New: ``fminus``
- New: ``forbetterorforworse``
- New: ``girlgenius``
- New: ``hijinksensue``
- New: ``joelovescrappymovies``
- New: ``magpieluck``
- New: ``nonsequitur``
- New: ``overcompensating``
- New: ``pluggers``
- New: ``tankmcnamara``
- New: ``theboondocks``
- New: ``thedreamer``
- New: ``wondermark``
- New: ``yehudamoon``
- Update ``playervsplayer`` to not miss comics on days with blog posts.
- Update ``questionablecontent`` to include text below image.
- Update ``kalscartoon`` after target site change.
- Update ``butternutsquash`` after target site change.


v1.0.0 (2010-01-27)
===================

A week has gone, and here is the 1.0.0 final release. Enjoy :-)

**Crawlers**

- Update ``uvod`` crawler to use new feed.


v1.0.0.rc2 (2010-01-19)
=======================

Second release candidate for 1.0.0. Again, I will bump to 1.0.0 in a week if no
new issues arises.

**Bugfixes**

- Make ``core/0006`` migration work on the sqlite3 backend.


v1.0.0.rc1 (2010-01-17)
=======================

First release, so no list of changes. Will bump to 1.0.0 in a week if no issues
arise. Please report any problems at http://github.com/jodal/comics/issues.

Development on *comics* as a Python/Django project started in February 2007, so
this release has been almost three years in the making. Far too long, and I
promise it won't be three years until the next release.
