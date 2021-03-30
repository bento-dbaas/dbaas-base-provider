ifneq (,$(wildcard ./.env))
    include .env
    export
endif

.PHONY: clean-pyc clean-build docs clean

help:
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "test - run tests quickly with the default Python"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "release - package and upload a release"
	@echo "sdist - package
	@echo "develop - enable development mode"

clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

test:
	coverage run --source=./ -m unittest discover --start-directory ./tests -p "*.py"
	coverage json
	coverage report

release:
	python setup.py sdist bdist_wheel
	twine upload dist/*

release_globo:
	python setup.py sdist bdist_wheel
	twine upload --repository-url ${GLOBO_INTERNAL_PYPI_URL} dist/*

dist: clean
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

develop:
	python setup.py develop