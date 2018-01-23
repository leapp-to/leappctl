from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='leappctl',
    version='0.0.1',
    description='A control interface for leapp-daemon',
    long_description=long_description,
    url='https://github.com/leapp-to/leappctl',
    author='Red Hat',
    author_email='leapp-devel@redhat.com',
    license="GPLv2+",
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'leappctl=leappctl.cli:main',
        ],
    },
)
