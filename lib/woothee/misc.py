# -*- coding: utf-8 -*-
from __future__ import (
    division, print_function,
    absolute_import, unicode_literals
)

import re
from . import dataset
from . import util


def challenge_desktoptools(ua, result):
    if 'AppleSyndication/' in ua:
        data = dataset.get('SafariRSSReader')
    elif 'compatible; Google Desktop/' in ua:
        data = dataset.get('GoogleDesktop')
    elif 'Windows-RSS-Platform' in ua:
        data = dataset.get('WindowsRSSReader')
    else:
        return False
    util.update_map(result, data)
    return True


def challenge_smartphone_patterns(ua, result):
    if 'CFNetwork/' in ua:
        data = dataset.get('iOS')
        util.update_category(result, data[dataset.KEY_CATEGORY])
        util.update_os(result, data[dataset.KEY_NAME])
        return True
    return False


def challenge_http_library(ua, result):

    regex_apache = re.compile(
        '^(?:Apache-HttpClient/|Jakarta Commons-HttpClient/|Java/)'
    )
    regex_php_product = re.compile(
        '^(?:PHP|WordPress|CakePHP|PukiWiki|PECL::HTTP)(?:/| |$)'
    )
    regex_pear = re.compile(
        '(?:PEAR |)HTTP_Request(?: class|2)'
    )
    regex_perl_library = re.compile(
        '^(?:libwww-perl|WWW-Mechanize|LWP::Simple|LWP |lwp-trivial)'
    )

    if regex_apache.search(ua) or re.search('[- ]HttpClient(/|$)', ua):
        data, version = dataset.get('HTTPLibrary'), 'Java'
    elif 'Java(TM) 2 Runtime Environment,' in ua:
        data, version = dataset.get('HTTPLibrary'), 'Java'
    elif re.search('^Wget', ua):
        data, version = dataset.get('HTTPLibrary'), 'wget'
    elif regex_perl_library.search(ua):
        data, version = dataset.get('HTTPLibrary'), 'perl'
    elif re.search('^(?:Ruby|feedzirra|Typhoeus)', ua):
        data, version = dataset.get('HTTPLibrary'), 'ruby'
    elif re.search('^(?:Python-urllib/|Twisted )', ua):
        data, version = dataset.get('HTTPLibrary'), 'python'
    elif regex_php_product.search(ua) or regex_pear.search(ua):
        data, version = dataset.get('HTTPLibrary'), 'php'
    else:
        return False
    util.update_map(result, data)
    util.update_version(result, version)
    return True


def challenge_maybe_rss_reader(ua, result):
    if re.search('rss(?:reader|bar|[-_ /;()]|[ +]*/)', ua, re.I) or\
            re.search('headline-reader', ua, re.I):
        data = dataset.get('VariousRSSReader')
    elif 'cococ/' in ua:
        data = dataset.get('VariousRSSReader')
    else:
        return False
    util.update_map(result, data)
    return True
