# Stubs for woothee (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Text, AnyStr, Tuple, Dict

VERSION: Tuple
FILLED: Dict[Text, Text]

def parse(useragent: AnyStr) -> Dict[AnyStr, AnyStr]: ...
def is_crawler(useragent: AnyStr) -> bool: ...
def exec_parse(useragent: AnyStr) -> Dict[AnyStr, AnyStr]: ...
def try_crawler(useragent: AnyStr, result: Dict[AnyStr, AnyStr]) -> bool: ...
def try_browser(useragent: AnyStr, result: Dict[AnyStr, AnyStr]) -> bool: ...
def try_os(useragent: AnyStr, result: Dict[AnyStr, AnyStr]) -> bool: ...
def try_mobilephone(useragent: AnyStr, result: Dict[AnyStr, AnyStr]) -> bool: ...
def try_appliance(useragent: AnyStr, result: Dict[AnyStr, AnyStr]) -> bool: ...
def try_misc(useragent: AnyStr, result: Dict[AnyStr, AnyStr]) -> bool: ...
def try_rare_cases(useragent: AnyStr, result: Dict[AnyStr, AnyStr]) -> bool: ...
def fill_result(result: Dict[AnyStr, AnyStr]) -> Dict[AnyStr, AnyStr]: ...