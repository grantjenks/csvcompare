CSVCompare: Compare CSV Files
=============================

.. image:: https://api.travis-ci.org/grantjenks/csvcompare.svg
    :target: http://www.grantjenks.com/docs/csvcompare/

`CSVCompare`_ is an Apache2 licensed module for CSV file comparison.

TODO
----

- Publish to pypi
- PyInstaller
- REST interface
- Package django app with web interface
- docs

Review
------

- Missing diff re: column
- setup.py
  - register command
  - sdist command
  - upload command
- MANIFEST.in file
- tox.ini file
- .travis.yml file

Release Workflow
................

- Make changes.
- Bump version.
- tox
- git commit -m "Bump version to ___"
- git tag -a v___ abchash -m v___
- git push
- git push --tags
- python setup.py sdist upload
- cd docs && make html
- Upload docs

Features
--------

- Pure-Python
- Fully Documented
- 100% Test Coverage
- Developed on Python 2.7
- Tested on CPython 2.6, 2.7, 3.2, 3.3, 3.4 and PyPy 2.5+, PyPy3 2.4+

Quickstart
----------

Installing CSVCompare is simple with
`pip <http://www.pip-installer.org/>`_::

    $ pip install csvcompare

You can access documentation in the interpreter with Python's built-in help
function::

    >>> import csvcompare
    >>> help(csvcompare)

Tutorial
--------

TODO

Reference and Indices
---------------------

* `CSVCopmare Documentation`_
* `CSVCompare at PyPI`_
* `CSVCompare at Github`_
* `CSVCompare Issue Tracker`_

.. _`CSVCompare Documentation`: http://www.grantjenks.com/docs/csvcompare/
.. _`CSVCompare at PyPI`: https://pypi.python.org/pypi/csvcompare
.. _`CSVCompare at Github`: https://github.com/grantjenks/csvcompare
.. _`CSVCompare Issue Tracker`: https://github.com/grantjenks/csvcompare/issues

CSVCompare License
------------------

Copyright 2015 Grant Jenks

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
