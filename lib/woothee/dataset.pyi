# Stubs for woothee.dataset (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Text, List, Dict

KEY_LABEL: Text
KEY_NAME: Text
KEY_TYPE: Text
KEY_CATEGORY: Text
KEY_OS: Text
KEY_OS_VERSION: Text
KEY_VENDOR: Text
KEY_VERSION: Text
TYPE_BROWSER: Text
TYPE_OS: Text
TYPE_FULL: Text
CATEGORY_PC: Text
CATEGORY_SMARTPHONE: Text
CATEGORY_MOBILEPHONE: Text
CATEGORY_CRAWLER: Text
CATEGORY_APPLIANCE: Text
CATEGORY_MISC: Text
ATTRIBUTE_NAME: Text
ATTRIBUTE_CATEGORY: Text
ATTRIBUTE_OS: Text
ATTRIBUTE_OS_VERSION: Text
ATTRIBUTE_VENDOR: Text
ATTRIBUTE_VERSION: Text
VALUE_UNKNOWN: Text
CATEGORY_LIST: List[Text]
ATTRIBUTE_LIST: List[Text]
DATASET: Dict[Text, Text]

def get(label: Text) -> Dict[Text, Text]: ...
