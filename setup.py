import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='abel',
    version='0.0.1',
    author='Hunan Rostomyan',
    author_email='hunan131@gmail.com',
    description='Machine learning components',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hunan-rostomyan/abel',
    packages=setuptools.find_packages(),
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ),
)