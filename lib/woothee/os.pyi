# Stubs for woothee.os (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Dict, AnyStr

def challenge_windows(ua: AnyStr, result: Dict[AnyStr, AnyStr]) -> bool: ...
def challenge_osx(ua: AnyStr, result: Dict[AnyStr, AnyStr]) -> bool: ...
def challenge_linux(ua: AnyStr, result: Dict[AnyStr, AnyStr]) -> bool: ...
def challenge_smartphone(ua: AnyStr, result: Dict[AnyStr, AnyStr]) -> bool: ...
def challenge_mobilephone(ua: AnyStr, result: Dict[AnyStr, AnyStr]) -> bool: ...
def challenge_appliance(ua: AnyStr, result: Dict[AnyStr, AnyStr]) -> bool: ...
def challenge_misc(ua: AnyStr, result: Dict[AnyStr, AnyStr]) -> bool: ...
