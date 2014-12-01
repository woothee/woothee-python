# -*- coding: utf-8 -*-
from __future__ import (division, print_function,
                        absolute_import, unicode_literals)
import re

from . import dataset
from . import util


def challenge_playstation(ua, result):

    data = None
    os_version = None
    if 'PSP (PlayStation Portable);' in ua:
        data = dataset.get('PSP')
        regex = re.compile(r"PSP \(PlayStation Portable\); ([.0-9]+)\)")
        m = regex.search(ua)
        if m:
            os_version = m.group(1)
    elif 'PlayStation Vita' in ua:
        data = dataset.get('PSVita')
        regex = re.compile(r"PlayStation Vita ([.0-9]+)\)")
        m = regex.search(ua)
        if m:
            os_version = m.group(1)
    elif 'PLAYSTATION 3 ' in ua or 'PLAYSTATION 3;' in ua:
        data = dataset.get('PS3')
        regex = re.compile(r"PLAYSTATION 3;? ([.0-9]+)\)")
        m = regex.search(ua)
        if m:
            os_version = m.group(1)
    elif 'PlayStation 4 ' in ua:
        data = dataset.get('PS4')
        regex = re.compile(r"PlayStation 4 ([.0-9]+)\)")
        m = regex.search(ua)
        if m:
            os_version = m.group(1)
    else:
        return False
    util.update_map(result, data)
    if os_version:
        util.update_os_version(result, os_version)
    return True


def challenge_nintendo(ua, result):
    if 'Nintendo 3DS;' in ua:
        data = dataset.get('Nintendo3DS')
    elif 'Nintendo DSi;' in ua:
        data = dataset.get('NintendoDSi')
    elif 'Nintendo Wii;' in ua:
        data = dataset.get('NintendoWii')
    elif '(Nintendo WiiU)' in ua:
        data = dataset.get('NintendoWiiU')
    else:
        return False
    util.update_map(result, data)
    return True


def challenge_digitaltv(ua, result):
    if 'InettvBrowser/' in ua:
        data = dataset.get('DigitalTV')
    else:
        return False
    util.update_map(result, data)
    return True
