Woothee python
==============

|travis| |coveralls| |downloads| |version| |license|

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

1.4.0(May 17, 2016)
~~~~~~~~~~~~~~~~~~~~

* Add suuport for Vivaldi

1.3.0(Jan 7, 2016)
~~~~~~~~~~~~~~~~~~~~

* Add suuport for Firefox for iOS

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


.. |travis| image:: https://travis-ci.org/woothee/woothee-python.svg?branch=master
    :target: https://travis-ci.org/woothee/woothee-python
    :alt: travis-ci.org

.. |coveralls| image:: https://coveralls.io/repos/woothee/woothee-python/badge.png
    :target: https://coveralls.io/r/woothee/woothee-python
    :alt: coveralls.io

.. |downloads| image:: https://img.shields.io/pypi/dm/woothee.svg
    :target: http://pypi.python.org/pypi/woothee/
    :alt: downloads

.. |version| image:: https://img.shields.io/pypi/v/woothee.svg
    :target: http://pypi.python.org/pypi/woothee/
    :alt: latest version

.. |license| image:: https://img.shields.io/pypi/l/woothee.svg
    :target: http://pypi.python.org/pypi/woothee/
    :alt: license
