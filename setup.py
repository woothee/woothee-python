from setuptools import setup, Command

version = [s for s in open('lib/woothee/__init__.py').read().split('\n') if s.startswith('__version__ = ')][0].split(' = ')[1].replace("'", '')  # NOQA


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
    packages=['woothee'],
    package_dir={'': 'lib'},
    platforms='any',
    setup_requires=['PyYAML>=3.10'],
    test_suite='tests',
    cmdclass={'dataset': dataset_command},
)
