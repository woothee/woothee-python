# -*- coding: utf-8 -*-
from __future__ import (division, print_function,
                        absolute_import, unicode_literals)

import re
from . import dataset
from . import util


def challenge_msie(ua, result):
    if 'compatible; MSIE' not in ua and 'Trident/' not in ua\
            and 'IEMobile' not in ua:
        return False
    version = dataset.VALUE_UNKNOWN
    msie = re.search(r'MSIE ([.0-9]+);', ua)
    trident = re.search(
        r'Trident\/([.0-9]+);', ua)
    tridentVersion = re.search(r' rv:([.0-9]+)', ua)
    iemobile = re.search(r'IEMobile\/([.0-9]+);', ua)

    if msie:
        version = msie.group(1)
    elif trident and tridentVersion:
        version = tridentVersion.group(1)
    elif iemobile:
        version = iemobile.group(1)

    util.update_map(result, dataset.get('MSIE'))
    util.update_version(result, version)
    return True


def challenge_safari_chrome(ua, result):
    if 'Safari/' not in ua:
        return False
    version = dataset.VALUE_UNKNOWN

    # Edge
    obj = re.search('Edge\/([.0-9]+)', ua)
    if obj:
        version = obj.group(1)
        util.update_map(result, dataset.get('Edge'))
        util.update_version(result, version)
        return True

    obj = re.search('FxiOS\/([.0-9]+)', ua)
    if obj:
        version = obj.group(1)
        util.update_map(result, dataset.get('Firefox'))
        util.update_version(result, version)
        return True

    obj = re.search('(?:Chrome|CrMo|CriOS)/([.0-9]+)', ua)
    if obj:
        chromeVersion = obj.group(1)
        obj = re.search('OPR/([.0-9]+)', ua)
        if obj:
            # Opera (blink)
            version = obj.group(1)
            util.update_map(result, dataset.get('Opera'))
            util.update_version(result, version)
            return True

        # Chrome
        util.update_map(result, dataset.get('Chrome'))
        util.update_version(result, chromeVersion)
        return True

    # Safari
    obj = re.search('Version/([.0-9]+)', ua)
    if obj:
        version = obj.group(1)
    util.update_map(result, dataset.get('Safari'))
    util.update_version(result, version)
    return True


def challenge_firefox(ua, result):
    if 'Firefox/' not in ua:
        return False
    obj = re.search('Firefox/([.0-9]+)', ua)
    version = obj.group(1) if obj else dataset.VALUE_UNKNOWN
    util.update_map(result, dataset.get('Firefox'))
    util.update_version(result, version)
    return True


def challenge_opera(ua, result):
    if 'Opera' not in ua:
        return False
    obj = re.search('Version/([.0-9]+)', ua)
    version = dataset.VALUE_UNKNOWN
    if obj:
        version = obj.group(1)
    else:
        obj = re.search('Opera[/ ]([.0-9]+)', ua)
        if obj:
            version = obj.group(1)
    util.update_map(result, dataset.get('Opera'))
    util.update_version(result, version)
    return True


def challenge_webview(ua, result):
    obj = re.search('iP(?:hone;|ad;|od) .*like Mac OS X', ua)
    # iOS
    if not obj or 'Safari/' in ua:
        return False

    obj = re.search('Version\/([.0-9]+)', ua)
    version = obj.group(1) if obj else dataset.VALUE_UNKNOWN
    util.update_map(result, dataset.get('Webview'))
    util.update_version(result, version)
    return True


def challenge_sleipnir(ua, result):
    if 'Sleipnir/' not in ua:
        return False
    obj = re.search('Sleipnir/([.0-9]+)', ua)
    version = obj.group(1) if obj else dataset.VALUE_UNKNOWN
    util.update_map(result, dataset.get('Sleipnir'))
    util.update_version(result, version)
    # Sleipnir's user-agent doesn't contain Windows version,
    # so put 'Windows UNKNOWN Ver'.
    # Sleipnir is IE component browser, so for Windows only.
    win = dataset.get('Win')
    util.update_category(result, win[dataset.KEY_CATEGORY])
    util.update_os(result, win[dataset.KEY_NAME])
    return True


def challenge_vivaldi(ua, result):
    if 'Vivaldi/' not in ua:
        return False

    obj = re.search('Vivaldi/([.0-9]+)', ua)
    version = obj.group(1) if obj else dataset.VALUE_UNKNOWN
    util.update_map(result, dataset.get('Vivaldi'))
    util.update_version(result, version)
    return True
