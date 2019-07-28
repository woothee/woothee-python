# -*- coding: utf-8 -*-

import os
import re
import sys
from setuptools import setup, Command, find_packages


with open(os.path.join('lib', 'woothee', '__init__.py'), 'r') as f:
    version = re.compile(
        r".*__version__ = '(.*?)'", re.S).match(f.read()).group(1)

with open('README.rst', 'r') as f:
    long_description = f.read()

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Web Environment",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Topic :: Internet :: WWW/HTTP",
    "Topic :: Software Development :: Libraries :: Python Modules",
]


install_requires = ['six>=1.8.0']

if sys.version_info < (3, 5):
    install_requires.append('typing')


class DatasetCommand(Command):

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
    description='Cross-language UserAgent classifier library, python implementation',  # NOQA
    author='tell-k',
    author_email='ffk2005@gmail.com',
    url='https://github.com/woothee/woothee-python',
    license='Apache License 2.0',
    packages=find_packages('lib'),
    package_dir={'': 'lib'},
    package_data={
        'woothee': ['py.typed', '*.pyi'],
    },
    platforms='any',
    install_requires=install_requires,
    setup_requires=['PyYAML>=3.10', 'six>=1.8.0', 'pytest-runner'],
    tests_require=['pytest', 'pytest-cov', 'pytest-mock'],
    long_description=long_description,
    classifiers=classifiers,
    keywords=['web', 'user-agent', 'parser'],
    cmdclass={'dataset': DatasetCommand},
)
