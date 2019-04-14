# Stubs for woothee.browser (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Dict, AnyStr

def challenge_msie(ua: AnyStr, result: Dict[AnyStr, AnyStr]) -> bool: ...
def challenge_yandexbrowser(ua: AnyStr, result: Dict[AnyStr, AnyStr]) -> bool: ...
def challenge_safari_chrome(ua: AnyStr, result: Dict[AnyStr, AnyStr]) -> bool: ...
def challenge_firefox(ua: AnyStr, result: Dict[AnyStr, AnyStr]) -> bool: ...
def challenge_opera(ua: AnyStr, result: Dict[AnyStr, AnyStr]) -> bool: ...
def challenge_webview(ua: AnyStr, result: Dict[AnyStr, AnyStr]) -> bool: ...
def challenge_sleipnir(ua: AnyStr, result: Dict[AnyStr, AnyStr]) -> bool: ...
def challenge_vivaldi(ua: AnyStr, result: Dict[AnyStr, AnyStr]) -> bool: ...