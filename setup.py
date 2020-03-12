from __future__ import division, absolute_import
from setuptools import setup, find_packages


setup(
    name='journal2gelf',
    version='2.2.0',
    description='Export structured log records from a systemd journal and send them to a Graylog server.',
    url='https://github.com/eryx12o45/journal2gelf',
    author='Eryx',
    author_email='eryx@gmx.net',
    license='MIT',
    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'journal2gelf = journal2gelf:main',
        ],
    }, install_requires=['systemd']
)
