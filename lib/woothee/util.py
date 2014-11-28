# -*- coding: utf-8 -*-
from __future__ import (division, print_function,
                        absolute_import, unicode_literals)
import six

from . import dataset


def update_map(target, source):
    for key in six.iterkeys(source):
        if key == dataset.KEY_LABEL or key == dataset.KEY_TYPE:
            continue
        if len(source[key]) > 0:
            target[key] = source[key]


def update_category(target, category):
    target[dataset.ATTRIBUTE_CATEGORY] = category


def update_version(target, version):
    target[dataset.ATTRIBUTE_VERSION] = version


def update_os(target, os):
    target[dataset.ATTRIBUTE_OS] = os


def update_os_version(target, version):
    target[dataset.ATTRIBUTE_OS_VERSION] = version
