Woothee python
==============

|github actions| |coveralls| |version| |license|

The Python implementation of Project Woothee, which is multi-language
user-agent strings parsers.

https://github.com/woothee/woothee

Installation
------------

::

   $ pip install woothee

Usage
-----

Parsing user-agent
~~~~~~~~~~~~~~~~~~

.. code:: python

    import woothee
    woothee.parse("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)")
    # => {'name': 'Internet Explorer', 'category': 'pc', 'os': 'Windows 7', 'version': '8.0', 'vendor': 'Microsoft', 'os_version': 'NT 6.1'}

Parse user-agent string and returns a object with keys ``name``, ``category``, ``os``, ``version``, ``vendor`` and ``os_version``.

For unknown user-agent (or partially failed to parse), result objects
may have value 'UNKNOWN'.

* ``category``

  * labels of user terminal type, one of 'pc', 'smartphone', 'mobilephone', 'appliance', 'crawler' or 'misc' (or 'UNKNOWN')

* ``name``

  * the name of browser, like 'Internet Explorer', 'Firefox', 'GoogleBot'

* ``version``

  * version string, like '8.0' for IE, '9.0.1' for Firefix, '0.2.149.27' for Chrome, and so on

* ``os``

  * ex: 'Windows 7', 'Mac OSX', 'iPhone', 'iPad', 'Android'
  * This field used to indicate cellar phone carrier for category 'mobilephone'

* ``vendor``

  * optional field, shows browser vendor

* ``os_version``

  * optional field, shows version of operating systems

Finding crawlers (almost all, not all) in fast
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   woothee.is_crawler('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)')
   # => False

Try to see useragent's category is 'crawler' or not, by casual(fast)
method. Minor case of crawlers is not tested in this method. To check
crawler strictly, use ``woothee.parse(str)['category'] == 'crawler'``.

Authors
-------

* UEDA Tetsuhiro (najeira)
* TAGOMORI Satoshi tagomoris@gmail.com
* tell-k ffk2005@gmail.com

License
-------

Copyright 2012- TAGOMORI Satoshi (tagomoris)

Licensed under the Apache License, Version 2.0 (the "License"); you may
not use this file except in compliance with the License. You may obtain
a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

History
-------

1.12.0, 1.12.1(not publish in PyPI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **drop support Python2 and Python3.5**
* `#23 support woothee v1.12 <https://github.com/woothee/woothee-python/pull/23>`_.

  * Add supoort samsugn browser
  * Add support Google bot


1.11.0(not publish in PyPI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `#18 support woothee v1.11 <https://github.com/woothee/woothee-python/pull/18>`_.

  * Add support GSA

1.10.1(Aug 8, 2019)
~~~~~~~~~~~~~~~~~~~~

* `#16 drop support Python3.4 <https://github.com/woothee/woothee-python/pull/16>`_.

1.10.0(Apr 14, 2019)
~~~~~~~~~~~~~~~~~~~~

* `#15 Support for v1.10.0 <https://github.com/woothee/woothee-python/pull/15>`_

1.8.0(Jul 5, 2018)
~~~~~~~~~~~~~~~~~~~~

* `#14 Drop support Python 2.6 and Python 3.2 <https://github.com/woothee/woothee-python/pull/14>`_.
* `#13 Add support for Yandex Browser <https://github.com/woothee/woothee-python/pull/13>`_. Thanks to hhatto .

1.7.0(May 7, 2017)
~~~~~~~~~~~~~~~~~~~~

* `#12 Release v1.7.0 <https://github.com/woothee/woothee-python/pull/12>`_
* Add support for WebView on Android.
* Add support for curl.
* Add support for trendictionbot crawler.
* Add support for Yeti 1.1.
* Compatible with Python 3.6.
* **Caution. We'll drop Python2.6 and python3.2 support in the next version.**

1.5.0(Aug 16, 2016)
~~~~~~~~~~~~~~~~~~~~

* `#11 Support BingPreview <https://github.com/woothee/woothee-python/pull/11>`_ Thanks to taise.

1.4.0(May 17, 2016)
~~~~~~~~~~~~~~~~~~~~

* Add support for Vivaldi

1.3.0(Jan 7, 2016)
~~~~~~~~~~~~~~~~~~~~

* Add support for Firefox for iOS

1.2.0(Aug 16, 2015)
~~~~~~~~~~~~~~~~~~~~

* Add support for Twitterbot
* Add support for webviews of mobile devices
* Add support for Windows 10 and Edge browser
* Add support for BlackBerry10

1.1.0(Mar 1, 2015)
~~~~~~~~~~~~~~~~~~~~
* `#9 Test blank cases <https://github.com/woothee/woothee-python/pull/9>`_ Thanks to yuya-takeyama.

1.0.0(Jan 20, 2015)
~~~~~~~~~~~~~~~~~~~~
* First release


.. |github actions| image:: https://github.com/woothee/woothee-python/workflows/Python%20package/badge.svg
    :target: https://github.com/woothee/woothee-python/actions
    :alt: GitHub Actions build status

.. |coveralls| image:: https://coveralls.io/repos/woothee/woothee-python/badge.png
    :target: https://coveralls.io/r/woothee/woothee-python
    :alt: coveralls.io

.. |version| image:: https://img.shields.io/pypi/v/woothee.svg
    :target: http://pypi.python.org/pypi/woothee/
    :alt: latest version

.. |license| image:: https://img.shields.io/pypi/l/woothee.svg
    :target: http://pypi.python.org/pypi/woothee/
    :alt: license
