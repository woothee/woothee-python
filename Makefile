all: test

TIMESTAMP=$(shell date +%Y%m%d-%H%M%S)

lib/woothee/dataset.py: woothee/dataset.yaml
	python setup.py dataset
	sync; sync; sync

test: lib/woothee/dataset.py
	python setup.py test
