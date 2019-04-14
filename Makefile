.PHONY: test flake8 mypy autopep8
all: autopep8 test mypy flake8

TIMESTAMP=$(shell date +%Y%m%d-%H%M%S)

lib/woothee/dataset.py: woothee/dataset.yaml
	python setup.py dataset
	sync; sync; sync

test: lib/woothee/dataset.py
	python setup.py test

flake8:
	tox -eflake8

mypy:
	tox -emypy

autopep8:
	tox -eautopep8
