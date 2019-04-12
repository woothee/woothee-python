# -*- coding: utf-8 -*-

KEY_LABEL = 'label'
KEY_NAME = 'name'
KEY_TYPE = 'type'
KEY_CATEGORY = 'category'
KEY_OS = 'os'
KEY_OS_VERSION = 'os_version'
KEY_VENDOR = 'vendor'
KEY_VERSION = 'version'

TYPE_BROWSER = 'browser'
TYPE_OS = 'os'
TYPE_FULL = 'full'

CATEGORY_PC = 'pc'
CATEGORY_SMARTPHONE = 'smartphone'
CATEGORY_MOBILEPHONE = 'mobilephone'
CATEGORY_CRAWLER = 'crawler'
CATEGORY_APPLIANCE = 'appliance'
CATEGORY_MISC = 'misc'

ATTRIBUTE_NAME = 'name'
ATTRIBUTE_CATEGORY = 'category'
ATTRIBUTE_OS = 'os'
ATTRIBUTE_OS_VERSION = 'os_version'
ATTRIBUTE_VENDOR = 'vendor'
ATTRIBUTE_VERSION = 'version'

VALUE_UNKNOWN = 'UNKNOWN'

CATEGORY_LIST = [
    CATEGORY_PC, CATEGORY_SMARTPHONE, CATEGORY_MOBILEPHONE,
    CATEGORY_CRAWLER, CATEGORY_APPLIANCE, CATEGORY_MISC, VALUE_UNKNOWN
]
ATTRIBUTE_LIST = [
    ATTRIBUTE_NAME, ATTRIBUTE_CATEGORY, ATTRIBUTE_OS,
    ATTRIBUTE_VENDOR, ATTRIBUTE_VERSION, ATTRIBUTE_OS_VERSION
]

DATASET = {}


def _init():
    # GENERATED from dataset.yaml at Fri Apr 12 23:12:13 2019 by tell_k
    obj = {'label': 'MSIE', 'name': 'Internet Explorer', 'type': 'browser'}  # NOQA
    obj['vendor'] = 'Microsoft'
    DATASET[obj['label']] = obj
    obj = {'label': 'Edge', 'name': 'Edge', 'type': 'browser'}  # NOQA
    obj['vendor'] = 'Microsoft'
    DATASET[obj['label']] = obj
    obj = {'label': 'Chrome', 'name': 'Chrome', 'type': 'browser'}  # NOQA
    obj['vendor'] = 'Google'
    DATASET[obj['label']] = obj
    obj = {'label': 'Safari', 'name': 'Safari', 'type': 'browser'}  # NOQA
    obj['vendor'] = 'Apple'
    DATASET[obj['label']] = obj
    obj = {'label': 'Firefox', 'name': 'Firefox', 'type': 'browser'}  # NOQA
    obj['vendor'] = 'Mozilla'
    DATASET[obj['label']] = obj
    obj = {'label': 'Opera', 'name': 'Opera', 'type': 'browser'}  # NOQA
    obj['vendor'] = 'Opera'
    DATASET[obj['label']] = obj
    obj = {'label': 'Vivaldi', 'name': 'Vivaldi', 'type': 'browser'}  # NOQA
    obj['vendor'] = 'Vivaldi Technologies'
    DATASET[obj['label']] = obj
    obj = {'label': 'Sleipnir', 'name': 'Sleipnir', 'type': 'browser'}  # NOQA
    obj['vendor'] = 'Fenrir Inc.'
    DATASET[obj['label']] = obj
    obj = {'label': 'Webview', 'name': 'Webview', 'type': 'browser'}  # NOQA
    obj['vendor'] = 'OS vendor'
    DATASET[obj['label']] = obj
    obj = {'label': 'YaBrowser', 'name': 'Yandex Browser', 'type': 'browser'}  # NOQA
    obj['vendor'] = 'Yandex'
    DATASET[obj['label']] = obj
    obj = {'label': 'Win', 'name': 'Windows UNKNOWN Ver', 'type': 'os'}  # NOQA
    obj['category'] = 'pc'
    DATASET[obj['label']] = obj
    obj = {'label': 'Win10', 'name': 'Windows 10', 'type': 'os'}  # NOQA
    obj['category'] = 'pc'
    DATASET[obj['label']] = obj
    obj = {'label': 'Win8.1', 'name': 'Windows 8.1', 'type': 'os'}  # NOQA
    obj['category'] = 'pc'
    DATASET[obj['label']] = obj
    obj = {'label': 'Win8', 'name': 'Windows 8', 'type': 'os'}  # NOQA
    obj['category'] = 'pc'
    DATASET[obj['label']] = obj
    obj = {'label': 'Win7', 'name': 'Windows 7', 'type': 'os'}  # NOQA
    obj['category'] = 'pc'
    DATASET[obj['label']] = obj
    obj = {'label': 'WinVista', 'name': 'Windows Vista', 'type': 'os'}  # NOQA
    obj['category'] = 'pc'
    DATASET[obj['label']] = obj
    obj = {'label': 'WinXP', 'name': 'Windows XP', 'type': 'os'}  # NOQA
    obj['category'] = 'pc'
    DATASET[obj['label']] = obj
    obj = {'label': 'Win2000', 'name': 'Windows 2000', 'type': 'os'}  # NOQA
    obj['category'] = 'pc'
    DATASET[obj['label']] = obj
    obj = {'label': 'WinNT4', 'name': 'Windows NT 4.0', 'type': 'os'}  # NOQA
    obj['category'] = 'pc'
    DATASET[obj['label']] = obj
    obj = {'label': 'WinMe', 'name': 'Windows Me', 'type': 'os'}  # NOQA
    obj['category'] = 'pc'
    DATASET[obj['label']] = obj
    obj = {'label': 'Win98', 'name': 'Windows 98', 'type': 'os'}  # NOQA
    obj['category'] = 'pc'
    DATASET[obj['label']] = obj
    obj = {'label': 'Win95', 'name': 'Windows 95', 'type': 'os'}  # NOQA
    obj['category'] = 'pc'
    DATASET[obj['label']] = obj
    obj = {'label': 'WinPhone', 'name': 'Windows Phone OS', 'type': 'os'}  # NOQA
    obj['category'] = 'smartphone'
    DATASET[obj['label']] = obj
    obj = {'label': 'WinCE', 'name': 'Windows CE', 'type': 'os'}  # NOQA
    obj['category'] = 'smartphone'
    DATASET[obj['label']] = obj
    obj = {'label': 'OSX', 'name': 'Mac OSX', 'type': 'os'}  # NOQA
    obj['category'] = 'pc'
    DATASET[obj['label']] = obj
    obj = {'label': 'MacOS', 'name': 'Mac OS Classic', 'type': 'os'}  # NOQA
    obj['category'] = 'pc'
    DATASET[obj['label']] = obj
    obj = {'label': 'Linux', 'name': 'Linux', 'type': 'os'}  # NOQA
    obj['category'] = 'pc'
    DATASET[obj['label']] = obj
    obj = {'label': 'BSD', 'name': 'BSD', 'type': 'os'}  # NOQA
    obj['category'] = 'pc'
    DATASET[obj['label']] = obj
    obj = {'label': 'ChromeOS', 'name': 'ChromeOS', 'type': 'os'}  # NOQA
    obj['category'] = 'pc'
    DATASET[obj['label']] = obj
    obj = {'label': 'Android', 'name': 'Android', 'type': 'os'}  # NOQA
    obj['category'] = 'smartphone'
    DATASET[obj['label']] = obj
    obj = {'label': 'iPhone', 'name': 'iPhone', 'type': 'os'}  # NOQA
    obj['category'] = 'smartphone'
    DATASET[obj['label']] = obj
    obj = {'label': 'iPad', 'name': 'iPad', 'type': 'os'}  # NOQA
    obj['category'] = 'smartphone'
    DATASET[obj['label']] = obj
    obj = {'label': 'iPod', 'name': 'iPod', 'type': 'os'}  # NOQA
    obj['category'] = 'smartphone'
    DATASET[obj['label']] = obj
    obj = {'label': 'iOS', 'name': 'iOS', 'type': 'os'}  # NOQA
    obj['category'] = 'smartphone'
    DATASET[obj['label']] = obj
    obj = {'label': 'FirefoxOS', 'name': 'Firefox OS', 'type': 'os'}  # NOQA
    obj['category'] = 'smartphone'
    DATASET[obj['label']] = obj
    obj = {'label': 'BlackBerry', 'name': 'BlackBerry', 'type': 'os'}  # NOQA
    obj['category'] = 'smartphone'
    DATASET[obj['label']] = obj
    obj = {'label': 'BlackBerry10', 'name': 'BlackBerry 10', 'type': 'os'}  # NOQA
    obj['category'] = 'smartphone'
    DATASET[obj['label']] = obj
    obj = {'label': 'docomo', 'name': 'docomo', 'type': 'full'}  # NOQA
    obj['vendor'] = 'docomo'
    obj['category'] = 'mobilephone'
    obj['os'] = 'docomo'
    DATASET[obj['label']] = obj
    obj = {'label': 'au', 'name': 'au by KDDI', 'type': 'full'}  # NOQA
    obj['vendor'] = 'au'
    obj['category'] = 'mobilephone'
    obj['os'] = 'au'
    DATASET[obj['label']] = obj
    obj = {'label': 'SoftBank', 'name': 'SoftBank Mobile', 'type': 'full'}  # NOQA
    obj['vendor'] = 'SoftBank'
    obj['category'] = 'mobilephone'
    obj['os'] = 'SoftBank'
    DATASET[obj['label']] = obj
    obj = {'label': 'willcom', 'name': 'WILLCOM', 'type': 'full'}  # NOQA
    obj['vendor'] = 'WILLCOM'
    obj['category'] = 'mobilephone'
    obj['os'] = 'WILLCOM'
    DATASET[obj['label']] = obj
    obj = {'label': 'jig', 'name': 'jig browser', 'type': 'full'}  # NOQA
    obj['category'] = 'mobilephone'
    obj['os'] = 'jig'
    DATASET[obj['label']] = obj
    obj = {'label': 'emobile', 'name': 'emobile', 'type': 'full'}  # NOQA
    obj['category'] = 'mobilephone'
    obj['os'] = 'emobile'
    DATASET[obj['label']] = obj
    obj = {'label': 'SymbianOS', 'name': 'SymbianOS', 'type': 'full'}  # NOQA
    obj['category'] = 'mobilephone'
    obj['os'] = 'SymbianOS'
    DATASET[obj['label']] = obj
    obj = {'label': 'MobileTranscoder', 'name': 'Mobile Transcoder', 'type': 'full'}  # NOQA
    obj['category'] = 'mobilephone'
    obj['os'] = 'Mobile Transcoder'
    DATASET[obj['label']] = obj
    obj = {'label': 'Nintendo3DS', 'name': 'Nintendo 3DS', 'type': 'full'}  # NOQA
    obj['vendor'] = 'Nintendo'
    obj['category'] = 'appliance'
    obj['os'] = 'Nintendo 3DS'
    DATASET[obj['label']] = obj
    obj = {'label': 'NintendoDSi', 'name': 'Nintendo DSi', 'type': 'full'}  # NOQA
    obj['vendor'] = 'Nintendo'
    obj['category'] = 'appliance'
    obj['os'] = 'Nintendo DSi'
    DATASET[obj['label']] = obj
    obj = {'label': 'NintendoWii', 'name': 'Nintendo Wii', 'type': 'full'}  # NOQA
    obj['vendor'] = 'Nintendo'
    obj['category'] = 'appliance'
    obj['os'] = 'Nintendo Wii'
    DATASET[obj['label']] = obj
    obj = {'label': 'NintendoWiiU', 'name': 'Nintendo Wii U', 'type': 'full'}  # NOQA
    obj['vendor'] = 'Nintendo'
    obj['category'] = 'appliance'
    obj['os'] = 'Nintendo Wii U'
    DATASET[obj['label']] = obj
    obj = {'label': 'PSP', 'name': 'PlayStation Portable', 'type': 'full'}  # NOQA
    obj['vendor'] = 'Sony'
    obj['category'] = 'appliance'
    obj['os'] = 'PlayStation Portable'
    DATASET[obj['label']] = obj
    obj = {'label': 'PSVita', 'name': 'PlayStation Vita', 'type': 'full'}  # NOQA
    obj['vendor'] = 'Sony'
    obj['category'] = 'appliance'
    obj['os'] = 'PlayStation Vita'
    DATASET[obj['label']] = obj
    obj = {'label': 'PS3', 'name': 'PlayStation 3', 'type': 'full'}  # NOQA
    obj['vendor'] = 'Sony'
    obj['category'] = 'appliance'
    obj['os'] = 'PlayStation 3'
    DATASET[obj['label']] = obj
    obj = {'label': 'PS4', 'name': 'PlayStation 4', 'type': 'full'}  # NOQA
    obj['vendor'] = 'Sony'
    obj['category'] = 'appliance'
    obj['os'] = 'PlayStation 4'
    DATASET[obj['label']] = obj
    obj = {'label': 'Xbox360', 'name': 'Xbox 360', 'type': 'full'}  # NOQA
    obj['vendor'] = 'Microsoft'
    obj['category'] = 'appliance'
    obj['os'] = 'Xbox 360'
    DATASET[obj['label']] = obj
    obj = {'label': 'XboxOne', 'name': 'Xbox One', 'type': 'full'}  # NOQA
    obj['vendor'] = 'Microsoft'
    obj['category'] = 'appliance'
    obj['os'] = 'Xbox One'
    DATASET[obj['label']] = obj
    obj = {'label': 'DigitalTV', 'name': 'InternetTVBrowser', 'type': 'full'}  # NOQA
    obj['category'] = 'appliance'
    obj['os'] = 'DigitalTV'
    DATASET[obj['label']] = obj
    obj = {'label': 'SafariRSSReader', 'name': 'Safari RSSReader', 'type': 'full'}  # NOQA
    obj['vendor'] = 'Apple'
    obj['category'] = 'misc'
    DATASET[obj['label']] = obj
    obj = {'label': 'GoogleDesktop', 'name': 'Google Desktop', 'type': 'full'}  # NOQA
    obj['vendor'] = 'Google'
    obj['category'] = 'misc'
    DATASET[obj['label']] = obj
    obj = {'label': 'WindowsRSSReader', 'name': 'Windows RSSReader', 'type': 'full'}  # NOQA
    obj['vendor'] = 'Microsoft'
    obj['category'] = 'misc'
    DATASET[obj['label']] = obj
    obj = {'label': 'VariousRSSReader', 'name': 'RSSReader', 'type': 'full'}  # NOQA
    obj['category'] = 'misc'
    DATASET[obj['label']] = obj
    obj = {'label': 'HTTPLibrary', 'name': 'HTTP Library', 'type': 'full'}  # NOQA
    obj['category'] = 'misc'
    DATASET[obj['label']] = obj
    obj = {'label': 'GoogleBot', 'name': 'Googlebot', 'type': 'full'}  # NOQA
    obj['category'] = 'crawler'
    DATASET[obj['label']] = obj
    obj = {'label': 'GoogleBotMobile', 'name': 'Googlebot Mobile', 'type': 'full'}  # NOQA
    obj['category'] = 'crawler'
    DATASET[obj['label']] = obj
    obj = {'label': 'GoogleMediaPartners', 'name': 'Google Mediapartners', 'type': 'full'}  # NOQA
    obj['category'] = 'crawler'
    DATASET[obj['label']] = obj
    obj = {'label': 'GoogleFeedFetcher', 'name': 'Google Feedfetcher', 'type': 'full'}  # NOQA
    obj['category'] = 'crawler'
    DATASET[obj['label']] = obj
    obj = {'label': 'GoogleAppEngine', 'name': 'Google AppEngine', 'type': 'full'}  # NOQA
    obj['category'] = 'crawler'
    DATASET[obj['label']] = obj
    obj = {'label': 'GoogleWebPreview', 'name': 'Google Web Preview', 'type': 'full'}  # NOQA
    obj['category'] = 'crawler'
    DATASET[obj['label']] = obj
    obj = {'label': 'YahooSlurp', 'name': 'Yahoo! Slurp', 'type': 'full'}  # NOQA
    obj['category'] = 'crawler'
    DATASET[obj['label']] = obj
    obj = {'label': 'YahooJP', 'name': 'Yahoo! Japan', 'type': 'full'}  # NOQA
    obj['category'] = 'crawler'
    DATASET[obj['label']] = obj
    obj = {'label': 'YahooPipes', 'name': 'Yahoo! Pipes', 'type': 'full'}  # NOQA
    obj['category'] = 'crawler'
    DATASET[obj['label']] = obj
    obj = {'label': 'Baiduspider', 'name': 'Baiduspider', 'type': 'full'}  # NOQA
    obj['category'] = 'crawler'
    DATASET[obj['label']] = obj
    obj = {'label': 'msnbot', 'name': 'msnbot', 'type': 'full'}  # NOQA
    obj['category'] = 'crawler'
    DATASET[obj['label']] = obj
    obj = {'label': 'bingbot', 'name': 'bingbot', 'type': 'full'}  # NOQA
    obj['category'] = 'crawler'
    DATASET[obj['label']] = obj
    obj = {'label': 'BingPreview', 'name': 'BingPreview', 'type': 'full'}  # NOQA
    obj['category'] = 'crawler'
    DATASET[obj['label']] = obj
    obj = {'label': 'Yeti', 'name': 'Naver Yeti', 'type': 'full'}  # NOQA
    obj['category'] = 'crawler'
    DATASET[obj['label']] = obj
    obj = {'label': 'FeedBurner', 'name': 'Google FeedBurner', 'type': 'full'}  # NOQA
    obj['category'] = 'crawler'
    DATASET[obj['label']] = obj
    obj = {'label': 'facebook', 'name': 'facebook', 'type': 'full'}  # NOQA
    obj['category'] = 'crawler'
    DATASET[obj['label']] = obj
    obj = {'label': 'twitter', 'name': 'twitter', 'type': 'full'}  # NOQA
    obj['category'] = 'crawler'
    DATASET[obj['label']] = obj
    obj = {'label': 'trendictionbot', 'name': 'trendiction', 'type': 'full'}  # NOQA
    obj['category'] = 'crawler'
    DATASET[obj['label']] = obj
    obj = {'label': 'mixi', 'name': 'mixi', 'type': 'full'}  # NOQA
    obj['category'] = 'crawler'
    DATASET[obj['label']] = obj
    obj = {'label': 'IndyLibrary', 'name': 'Indy Library', 'type': 'full'}  # NOQA
    obj['category'] = 'crawler'
    DATASET[obj['label']] = obj
    obj = {'label': 'ApplePubSub', 'name': 'Apple iCloud', 'type': 'full'}  # NOQA
    obj['category'] = 'crawler'
    DATASET[obj['label']] = obj
    obj = {'label': 'Genieo', 'name': 'Genieo Web Filter', 'type': 'full'}  # NOQA
    obj['category'] = 'crawler'
    DATASET[obj['label']] = obj
    obj = {'label': 'topsyButterfly', 'name': 'topsy Butterfly', 'type': 'full'}  # NOQA
    obj['category'] = 'crawler'
    DATASET[obj['label']] = obj
    obj = {'label': 'rogerbot', 'name': 'SeoMoz rogerbot', 'type': 'full'}  # NOQA
    obj['category'] = 'crawler'
    DATASET[obj['label']] = obj
    obj = {'label': 'AhrefsBot', 'name': 'ahref AhrefsBot', 'type': 'full'}  # NOQA
    obj['category'] = 'crawler'
    DATASET[obj['label']] = obj
    obj = {'label': 'radian6', 'name': 'salesforce radian6', 'type': 'full'}  # NOQA
    obj['category'] = 'crawler'
    DATASET[obj['label']] = obj
    obj = {'label': 'Hatena', 'name': 'Hatena', 'type': 'full'}  # NOQA
    obj['category'] = 'crawler'
    DATASET[obj['label']] = obj
    obj = {'label': 'goo', 'name': 'goo', 'type': 'full'}  # NOQA
    obj['category'] = 'crawler'
    DATASET[obj['label']] = obj
    obj = {'label': 'livedoorFeedFetcher', 'name': 'livedoor FeedFetcher', 'type': 'full'}  # NOQA
    obj['category'] = 'crawler'
    DATASET[obj['label']] = obj
    obj = {'label': 'VariousCrawler', 'name': 'misc crawler', 'type': 'full'}  # NOQA
    obj['category'] = 'crawler'
    DATASET[obj['label']] = obj


_init()


def get(label):
    return DATASET[label]
