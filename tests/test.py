# -*- coding:utf-8 -*-
from __future__ import (division, print_function,
                        absolute_import, unicode_literals)

import mock
import os
import sys
import unittest
import yaml

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_PATH, 'lib'))
TESTSET_DIR = os.path.join(BASE_PATH, 'woothee', 'testsets')

TARGETS = [
    ['crawler.yaml', 'Crawler'],
    ['crawler_google.yaml', 'Crawler/Google'],
    ['pc_windows.yaml', 'PC/Windows'],
    ['pc_misc.yaml', 'PC/Misc'],
    ['mobilephone_docomo.yaml', 'MobilePhone/docomo'],
    ['mobilephone_au.yaml', 'MobilePhone/au'],
    ['mobilephone_softbank.yaml', 'MobilePhone/softbank'],
    ['mobilephone_willcom.yaml', 'MobilePhone/willcom'],
    ['mobilephone_misc.yaml', 'MobilePhone/misc'],
    ['smartphone_ios.yaml', 'SmartPhone/ios'],
    ['smartphone_android.yaml', 'SmartPhone/android'],
    ['smartphone_misc.yaml', 'SmartPhone/misc'],
    ['appliance.yaml', 'Appliance'],
    ['pc_lowpriority.yaml', 'PC/LowPriority'],
    ['misc.yaml', 'Misc'],
    ['crawler_nonmajor.yaml', 'Crawler/NonMajor'],
    ['blank.yaml', 'Blank'],
]


class WootheeTest(unittest.TestCase):

    def test_contains_constants(self):
        from woothee import dataset
        self.assertEqual(dataset.ATTRIBUTE_NAME, 'name')

    def test_contains_const_list(self):
        from woothee import dataset
        self.assertEqual(
            dataset.ATTRIBUTE_LIST,
            [dataset.ATTRIBUTE_NAME, dataset.ATTRIBUTE_CATEGORY,
             dataset.ATTRIBUTE_OS, dataset.ATTRIBUTE_VENDOR,
             dataset.ATTRIBUTE_VERSION, dataset.ATTRIBUTE_OS_VERSION]
        )
        self.assertEqual(
            dataset.CATEGORY_LIST,
            [dataset.CATEGORY_PC, dataset.CATEGORY_SMARTPHONE,
             dataset.CATEGORY_MOBILEPHONE, dataset.CATEGORY_CRAWLER,
             dataset.CATEGORY_APPLIANCE, dataset.CATEGORY_MISC,
             dataset.VALUE_UNKNOWN]
        )

    def test_contains_dataset(self):
        from woothee import dataset
        self.assertEqual(dataset.get('GoogleBot')['name'], 'Googlebot')

    def test_should_be_read_from_each_modules_correctly(self):
        pass

    def test_testsets(self):
        import woothee

        check_attributes = ('name', 'category', 'os',
                            'version', 'vendor', 'os_version')

        def _can_assert(attribute, e):
            if attribute in ('name', 'category'):
                return True
            check_attributes = ('os', 'version', 'vendor', 'os_version')
            if attribute in check_attributes and attribute in e:
                return True
            return False

        for filename, groupname in TARGETS:
            with open(os.path.join(TESTSET_DIR, filename), 'rb') as fp:
                for es in yaml.load_all(fp):
                    for e in es:
                        r = woothee.parse(e['target'])
                        for attribute in check_attributes:

                            testname = groupname + (' test({0}): {1}'.format(
                                attribute, e['target']
                            ))
                            if _can_assert(attribute, e):
                                self.assertEqual(
                                    r[attribute],
                                    e[attribute],
                                    testname
                                )

    def test_non_provide_testsets(self):
        # This test pattern that does not exist in testsets.
        # The main purpose is that each logic to pass.
        # UserAgent is a dummy that does not exist in the world.

        import woothee

        # 48 line in lib/woothee/appliance.py
        self.assertEqual({
            "name": "Nintendo DSi",
            "version": "UNKNOWN",
            "os": "Nintendo DSi",
            "os_version": "UNKNOWN",
            "category": "appliance",
            "vendor": "Nintendo",
        }, woothee.parse("(Nintendo DSi; U; ja)"))

        # 50 line in lib/woothee/appliance.py
        self.assertEqual({
            "name": "Nintendo Wii",
            "version": "UNKNOWN",
            "os": "Nintendo Wii",
            "os_version": "UNKNOWN",
            "category": "appliance",
            "vendor": "Nintendo",
        }, woothee.parse("(Nintendo Wii; U; ; 3642; ja)"))

        # 26 line lib/woothee/browser.py
        self.assertEqual({
            "name": "Internet Explorer",
            "version": "11.0",
            "os": "Windows Phone OS",
            "os_version": "8.1",
            "category": "smartphone",
            "vendor": "Microsoft",
        }, woothee.parse(
            "Mozilla/5.0 (Windows Phone 8.1; ARM; Trident/7.0;"
            " Touch; IEMobile/11.0; NOKIA; Lumia 930) like Gecko"
        ))

        # 159 line lib/woothee/crawler.py
        self.assertEqual({
            "name": "UNKNOWN",
            "version": "UNKNOWN",
            "os": "UNKNOWN",
            "os_version": "UNKNOWN",
            "category": "UNKNOWN",
            "vendor": "UNKNOWN",
        }, woothee.parse("Data-Hotel-Cat/1.1"))

        # 74-75 line lib/woothee/mobilephone.py
        self.assertEqual({
            "name": "SymbianOS",
            "version": "UNKNOWN",
            "os": "SymbianOS",
            "os_version": "UNKNOWN",
            "category": "mobilephone",
            "vendor": "UNKNOWN",
        }, woothee.parse("SymbianOS/9.2;"))

        # 78-80 line lib/woothee/mobilephone.py
        self.assertEqual({
            "name": "Mobile Transcoder",
            "version": "Hatena",
            "os": "Mobile Transcoder",
            "os_version": "UNKNOWN",
            "category": "mobilephone",
            "vendor": "UNKNOWN",
        }, woothee.parse(
            "(compatible; Hatena-Mobile-Gateway/1.2;"
            " +http://mgw.hatena.ne.jp/help)"
        ))

        # 25-27 line lib/woothee/os.py
        self.assertEqual({
            "name": "UNKNOWN",
            "version": "UNKNOWN",
            "os": "Windows UNKNOWN Ver",
            "os_version": "UNKNOWN",
            "category": "pc",
            "vendor": "UNKNOWN",
        }, woothee.parse(
            "Mozilla/5.0 (Windows ; rv:8.0) Gecko/20111105 Thunderbird/8.0"
        ))

        # 49 line lib/woothee/os.py
        self.assertEqual({
            "name": "Internet Explorer",
            "version": "UNKNOWN",
            "os": "Windows NT 4.0",
            "os_version": "NT 4.0",
            "category": "pc",
            "vendor": "Microsoft",
        }, woothee.parse(
            "Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 4.0)"
        ))

        # 51 line lib/woothee/os.py
        self.assertEqual({
            "name": "Internet Explorer",
            "version": "6.0",
            "os": "Windows 98",
            "os_version": "98",
            "category": "pc",
            "vendor": "Microsoft",
        }, woothee.parse(
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98)"
        ))

        # 53 line lib/woothee/os.py
        self.assertEqual({
            "name": "Internet Explorer",
            "version": "5.50",
            "os": "Windows 95",
            "os_version": "95",
            "category": "pc",
            "vendor": "Microsoft",
        }, woothee.parse(
            "Mozilla/4.0 (compatible; MSIE 5.50; Windows 95; SiteKiosk 4.8)"
        ))

        # 121 line lib/woothee/os.py
        self.assertEqual({
            "name": "UNKNOWN",
            "version": "UNKNOWN",
            "os": "iPad",
            "os_version": "UNKNOWN",
            "category": "smartphone",
            "vendor": "UNKNOWN",
        }, woothee.parse("Mozilla/5.0 (iPad; "))

        # 123 line lib/woothee/os.py
        self.assertEqual({
            "name": "UNKNOWN",
            "version": "UNKNOWN",
            "os": "iPod",
            "os_version": "UNKNOWN",
            "category": "smartphone",
            "vendor": "UNKNOWN",
        }, woothee.parse("Mozilla/5.0 (iPod; "))

        # 183-185 line lib/woothee/os.py
        self.assertEqual({
            "name": "Mobile Transcoder",
            "version": "Naver",
            "os": "Mobile Transcoder",
            "os_version": "UNKNOWN",
            "category": "mobilephone",
            "vendor": "UNKNOWN",
        }, woothee.parse("Naver Transcoder"))


class TestIsCrawler(unittest.TestCase):

    def _getTarget(self):
        from woothee import is_crawler
        return is_crawler

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def test_false(self):
        self.assertFalse(self._callFUT(""))
        self.assertFalse(self._callFUT("-"))
        self.assertFalse(self._callFUT(None))
        self.assertFalse(self._callFUT(
            "Mozilla/5.0 (Windows NT 6.3; "
            "Trident/7.0; rv:11.0) like Gecko"
        ))

    def test_true(self):
        self.assertTrue(self._callFUT(
            "Mozilla/5.0 (compatible; Yahoo! Slurp;"
            " http://help.yahoo.com/help/us/ysearch/slurp)"
        ))


class TestTryRareCases(unittest.TestCase):
    """ challenge_smartphone_patterns in try_rare_cases is never return True.
    Because, "CFNetwork" is caught by the challenge_smartphone in try_os.
    Therefore, I have prepared the individual a test case

    Not need this function(challenge_smartphone_patterns) just maybe.
    """

    def _getTarget(self):
        from woothee import try_rare_cases
        return try_rare_cases

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    @mock.patch("woothee.browser.challenge_sleipnir")
    def test_challenge_smartphone_patterns(self, mock_sleipnir):
        result = {}
        self.assertTrue(self._callFUT("CFNetwork/", result))
        self.assertEqual({'category': 'smartphone', 'os': 'iOS'}, result)
        self.assertFalse(mock_sleipnir.called)

if __name__ == '__main__':
    unittest.main()
