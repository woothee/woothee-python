# -*- coding:utf-8 -*-
from __future__ import (division, print_function,
                        absolute_import, unicode_literals)
import os
import sys

import yaml
import pytest

from typing import Dict  # NOQA

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_PATH, 'lib'))  # type: ignore
TESTSET_DIR = os.path.join(BASE_PATH, 'woothee', 'testsets')

TARGETS = [
    ['appliance.yaml', 'Appliance'],
    ['blank.yaml', 'Blank'],
    ['crawler.yaml', 'Crawler'],
    ['crawler_google.yaml', 'Crawler/Google'],
    ['crawler_nonmajor.yaml', 'Crawler/NonMajor'],
    ['misc.yaml', 'Misc'],
    ['mobilephone_au.yaml', 'MobilePhone/au'],
    ['mobilephone_docomo.yaml', 'MobilePhone/docomo'],
    ['mobilephone_misc.yaml', 'MobilePhone/misc'],
    ['mobilephone_softbank.yaml', 'MobilePhone/softbank'],
    ['mobilephone_willcom.yaml', 'MobilePhone/willcom'],
    ['pc_lowpriority.yaml', 'PC/LowPriority'],
    ['pc_misc.yaml', 'PC/Misc'],
    ['pc_windows.yaml', 'PC/Windows'],
    ['smartphone_android.yaml', 'SmartPhone/android'],
    ['smartphone_ios.yaml', 'SmartPhone/ios'],
    ['smartphone_misc.yaml', 'SmartPhone/misc'],
]


def gen_test_cases():
    for filename, groupname in TARGETS:
        with open(os.path.join(TESTSET_DIR, filename), 'rb') as fp:
            for test_cases in yaml.safe_load_all(fp):
                for test_case in test_cases:
                    yield groupname, test_case


class TestDataset:

    def test_contains_constants(self):
        from woothee import dataset
        assert dataset.ATTRIBUTE_NAME == 'name'

    def test_contains_attribute_list(self):
        from woothee import dataset
        assert dataset.ATTRIBUTE_LIST == [
            dataset.ATTRIBUTE_NAME,
            dataset.ATTRIBUTE_CATEGORY,
            dataset.ATTRIBUTE_OS,
            dataset.ATTRIBUTE_VENDOR,
            dataset.ATTRIBUTE_VERSION,
            dataset.ATTRIBUTE_OS_VERSION
        ]

    def test_contains_category_list(self):
        from woothee import dataset

        assert dataset.CATEGORY_LIST == [
            dataset.CATEGORY_PC,
            dataset.CATEGORY_SMARTPHONE,
            dataset.CATEGORY_MOBILEPHONE,
            dataset.CATEGORY_CRAWLER,
            dataset.CATEGORY_APPLIANCE,
            dataset.CATEGORY_MISC,
            dataset.VALUE_UNKNOWN
        ]


class TestParse:

    @pytest.fixture()
    def target(self):
        from woothee import parse
        return parse

    @pytest.mark.parametrize(('groupname', 'test_case'), gen_test_cases())
    def test_testsets(self, target, groupname, test_case):
        ua_string = test_case.pop('target')
        expected = test_case

        parsed = target(ua_string)

        # Check only the attrs exists in the expected(=test_case).
        actual = {k: v for k, v in parsed.items() if k in expected}
        msg = '{0} test({1})'.format(groupname, ua_string)
        assert actual == expected, msg

    @pytest.mark.parametrize(('expected', 'ua_string'), [
        # 48 line in lib/woothee/appliance.py
        (
            {
                "name": "Nintendo DSi",
                "version": "UNKNOWN",
                "os": "Nintendo DSi",
                "os_version": "UNKNOWN",
                "category": "appliance",
                "vendor": "Nintendo",
            },
            "(Nintendo DSi; U; ja)"
        ),
        # 50 line in lib/woothee/appliance.py
        (
            {
                "name": "Nintendo Wii",
                "version": "UNKNOWN",
                "os": "Nintendo Wii",
                "os_version": "UNKNOWN",
                "category": "appliance",
                "vendor": "Nintendo",
            },
            "(Nintendo Wii; U; ; 3642; ja)"
        ),
        # 26 line lib/woothee/browser.py
        (
            {
                "name": "Internet Explorer",
                "version": "11.0",
                "os": "Windows Phone OS",
                "os_version": "8.1",
                "category": "smartphone",
                "vendor": "Microsoft",
            },
            (
                "Mozilla/5.0 (Windows Phone 8.1; ARM; Trident/7.0;"
                " Touch; IEMobile/11.0; NOKIA; Lumia 930) like Gecko"
            )
        ),
        # 159 line lib/woothee/crawler.py
        (
            {
                "name": "UNKNOWN",
                "version": "UNKNOWN",
                "os": "UNKNOWN",
                "os_version": "UNKNOWN",
                "category": "UNKNOWN",
                "vendor": "UNKNOWN",
            },
            "Data-Hotel-Cat/1.1"
        ),
        # 74-75 line lib/woothee/mobilephone.py
        (
            {
                "name": "SymbianOS",
                "version": "UNKNOWN",
                "os": "SymbianOS",
                "os_version": "UNKNOWN",
                "category": "mobilephone",
                "vendor": "UNKNOWN",
            },
            "SymbianOS/9.2;"
        ),
        # 78-80 line lib/woothee/mobilephone.py
        (
            {
                "name": "Mobile Transcoder",
                "version": "Hatena",
                "os": "Mobile Transcoder",
                "os_version": "UNKNOWN",
                "category": "mobilephone",
                "vendor": "UNKNOWN",
            },
            (
                "(compatible; Hatena-Mobile-Gateway/1.2;"
                " +http://mgw.hatena.ne.jp/help)"
            )
        ),
        # 25-27 line lib/woothee/os.py
        (
            {
                "name": "UNKNOWN",
                "version": "UNKNOWN",
                "os": "Windows UNKNOWN Ver",
                "os_version": "UNKNOWN",
                "category": "pc",
                "vendor": "UNKNOWN",
            },
            "Mozilla/5.0 (Windows ; rv:8.0) Gecko/20111105 Thunderbird/8.0"
        ),
        # 49 line lib/woothee/os.py
        (
            {
                "name": "Internet Explorer",
                "version": "UNKNOWN",
                "os": "Windows NT 4.0",
                "os_version": "NT 4.0",
                "category": "pc",
                "vendor": "Microsoft",
            },
            "Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 4.0)"
        ),
        # 51 line lib/woothee/os.py
        (
            {
                "name": "Internet Explorer",
                "version": "6.0",
                "os": "Windows 98",
                "os_version": "98",
                "category": "pc",
                "vendor": "Microsoft",
            },
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98)"
        ),
        # 53 line lib/woothee/os.py
        (
            {
                "name": "Internet Explorer",
                "version": "5.50",
                "os": "Windows 95",
                "os_version": "95",
                "category": "pc",
                "vendor": "Microsoft",
            },
            "Mozilla/4.0 (compatible; MSIE 5.50; Windows 95; SiteKiosk 4.8)"
        ),
        # 121 line lib/woothee/os.py
        (
            {
                "name": "UNKNOWN",
                "version": "UNKNOWN",
                "os": "iPad",
                "os_version": "UNKNOWN",
                "category": "smartphone",
                "vendor": "UNKNOWN",
            },
            "Mozilla/5.0 (iPad; "
        ),
        # 123 line lib/woothee/os.py
        (
            {
                "name": "UNKNOWN",
                "version": "UNKNOWN",
                "os": "iPod",
                "os_version": "UNKNOWN",
                "category": "smartphone",
                "vendor": "UNKNOWN",
            },
            "Mozilla/5.0 (iPod; "
        ),
        # 183-185 line lib/woothee/os.py
        (
            {
                "name": "Mobile Transcoder",
                "version": "Naver",
                "os": "Mobile Transcoder",
                "os_version": "UNKNOWN",
                "category": "mobilephone",
                "vendor": "UNKNOWN",
            },
            "Naver Transcoder"
        )
    ])
    def test_non_provide_testsets(self, target, expected, ua_string):
        # This test pattern that does not exist in testsets.
        # The main purpose is that each logic to pass.
        # UserAgent is a dummy that does not exist in the world.
        assert expected == target(ua_string)


class TestIsCrawler:

    @pytest.fixture
    def target(self):
        from woothee import is_crawler
        return is_crawler

    @pytest.mark.parametrize('ua_string', [
        "",
        "-",
        None,
        "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko"
    ])
    def test_false(self, target, ua_string):
        assert not target(ua_string)

    @pytest.mark.parametrize('ua_string', [
        ("Mozilla/5.0 (compatible; Yahoo! Slurp;"
         " http://help.yahoo.com/help/us/ysearch/slurp)"),
    ])
    def test_true(self, target, ua_string):
        assert target(ua_string)


class TestTryRareCases:
    """ challenge_smartphone_patterns in try_rare_cases is never return True.
    Because, "CFNetwork" is caught by the challenge_smartphone in try_os.
    Therefore, I have prepared the individual a test case

    Not need this function(challenge_smartphone_patterns) just maybe.
    """

    @pytest.fixture()
    def target(self):
        from woothee import try_rare_cases
        return try_rare_cases

    def test_challenge_smartphone_patterns(self, target, mocker):
        m = mocker.patch("woothee.browser.challenge_sleipnir")
        result = {}  # type: Dict[str, str]

        ret = target("CFNetwork/", result)

        expected = {
            'return_value': True,
            'result': {'category': 'smartphone', 'os': 'iOS'},
            'called_check': False,
        }
        actual = {
            'return_value': ret,
            'result': result,
            'called_check': m.called,
        }
        assert expected == actual
