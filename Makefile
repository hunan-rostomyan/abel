build:
	python3 setup.py sdist bdist_wheel

upload:
	python3 -m twine upload dist/*

install:
	python3 -m pip install --index-url https://test.pypi.org/simple/ abel

test:
	py.test --cov=abel --cov-report term-missing

clean:
	rm -rf dist
	rm -rf build
