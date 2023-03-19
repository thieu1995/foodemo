test-cov-unit:
	pytest --cov-report html --cov=foo tests

clean:
	rm -rf dist/


build:
	python -m build


test-release:
	twine upload --repository testpypi dist/*


release:
	twine upload --repository pypi dist/*