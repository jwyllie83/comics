***********
Development
***********

*comics* development is coordinated through `GitHub <http://github.com/>`_ and
the IRC channel ``#dailycomics`` at ``irc.freenode.net``.


How to contribute
=================

The easiest way to contribute to *comics* is to register as a user at GitHub,
fork `the comics project <http://github.com/jodal/comics>`_, and start hacking.
To get your changes back into *comics*' mainline, send a pull request to `jodal
at GitHub <http://github.com/jodal>`_, or send a mail to `comics@jodal.no
<mailto:comics@jodal.no>`_. Patches accompanied by tests and documentation
gives +5 karma and kudos. When hacking on *comics*, please follow the code
style and commit guidelines below.

All contributions must be granted under the same license as *comics* itself.


Code style
----------

- Follow :pep:`8` unless otherwise noted. `pep8.py
  <http://pypi.python.org/pypi/pep8/>`_ can be used to check your code against
  the guidelines, however remember that matching the style of the surrounding
  code is also important.

- Use four spaces for indentation, *never* tabs.

- Use CamelCase with initial caps for class names::

      ClassNameWithCamelCase

- Use underscore to split variable, function and method names for
  readability. Don't use CamelCase.

  ::

      lower_case_with_underscores

- Use the fact that empty strings, lists and tuples are False and don't compare
  boolean values using ``==`` and ``!=``.

- Follow whitespace rules as described in :pep:`8`. Good examples::

      spam(ham[1], {eggs: 2})
      spam(1)
      dict['key'] = list[index]

- Limit lines to 80 characters and avoid trailing whitespace. However note that
  wrapped lines should be *one* indentation level in from level above, except
  for ``if``, ``for``, ``with``, and ``while`` lines which should have two
  levels of indentation::

      if (foo and bar ...
              baz and foobar):
          a = 1

      from foobar import (foo, bar, ...
          baz)

- For consistency, prefer ``'`` over ``"`` for strings, unless the string
  contains ``'``.

- Take a look at :pep:`20` for a nice peek into a general mindset useful for
  Python coding.


Commit guidelines
-----------------

- Keep commits small and on topic, e.g. add one crawler per commit.

- Merge feature branches with ``--no-ff`` to keep track of the merge.

- When expanding API to accommodate new crawler features, commit API changes,
  then new crawlers in a separate commit.

- When changing existing API, commit API change and crawler changes in same
  commit. If this commit looks too big you should be working in a feature
  branch not a single commit.

- Same policy applies for non-crawler changes.


Data model
==========

*comics*' data model is very simple. The :mod:`comics.core` app consists of
three models; :class:`Comic <comics.core.models.Comic>`, :class:`Release
<comics.core.models.Release>`, and :class:`Image <comics.core.models.Image>`.
The :mod:`comics.sets` app adds an additional model named :class:`Set
<comics.sets.models.Set>`. Changes to the data model are managed using `South
<http://south.aeracode.org/>`_ database migrations. If you need to change the
models, please provide the needed migrations.

.. image:: _static/data_model.png

The above data model diagram was generated using the Django app
`django_extensions <http://code.google.com/p/django-command-extensions/>`_ and
the following command:

.. code-block:: sh

    python manage.py graph_models --settings=comics.settings.dev \
        --output=../docs/_static/data_model.png --group-models \
        core sets


Running tests
=============

*comics* got some tests, but far from full test coverage. If you write new or
improved tests for *comics*' functionality it will be greatly appreciated.

To run unit tests::

    python manage.py test --settings=comics.settings.testing

To run unit tests with statement coverage::

    python manage.py test --settings=comics.settings.coverage


Change specifications
=====================

When planning or doing larger changes to *comics*, notes may be added to the
documentation as a *change specification*.

.. toctree::
    :glob:

    specs/*


To-do list
==========

A loosely prioritized list of things to fix. Patches accepted.

``bin/smush``
    Process images with ``bin/smush`` to reduce their size 10-20% (without
    affecting their quality) and thus reducing page load time.
:mod:`comics.aggregator.command`
    Use comic week schedule to crawl less often on non-schedule days.
:mod:`comics.core.utils.navigation`
    Unit test and refactor.
