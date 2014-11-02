# -*- coding: utf-8 -*-

import os
import re
from setuptools import setup, Command, find_packages


with open(os.path.join('lib', 'woothee', '__init__.py'), 'r') as f:
    version = re.compile(
        r".*__version__ = '(.*?)'", re.S).match(f.read()).group(1)

with open('README.rst', 'r') as f:
    long_description = f.read()

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Web Environment"
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2"
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3"
    "Programming Language :: Python :: 3.2",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Topic :: Internet :: WWW/HTTP",
    "Topic :: Software Development :: Libraries :: Python Modules"
]


class dataset_command(Command):

    description = 'generate dataset.py'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import os
        import sys
        root_dir = os.path.dirname(os.path.abspath(__file__))
        scripts_dir = os.path.join(root_dir, 'scripts')
        sys.path.insert(0, scripts_dir)
        import dataset_yaml2py  # NOQA

setup(
    name='woothee',
    version=version,
    description='user-agent classificator',
    author='Najeira',
    author_email='najeira@gmail.com',
    url='https://github.com/woothee/woothee-python',
    license='http://www.apache.org/licenses/LICENSE-2.0',
    packages=find_packages('lib'),
    package_dir={'': 'lib'},
    platforms='any',
    install_requires=["six>=1.8.0"],
    setup_requires=['PyYAML>=3.10', "six>=1.8.0"],
    tests_require=['mock'],
    test_suite='tests',
    long_description=long_description,
    classifiers=classifiers,
    cmdclass={'dataset': dataset_command},
)
