#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

from vcardgen.version import __version__
from vcardgen import __doc__

setup(
    name='vcardgen',
    version=__version__,
    url='https://github.com/davidak/random-vcard-generator/',
    license='GPLv3',
    author='davidak',
    author_email='post@davidak.de',
    keywords = ('random vcard generator test import export'),
    platforms='any',
    description=__doc__,
    long_description=open('README.rst').read(),
    packages=['vcardgen'],
    entry_points = {
        'console_scripts': ['vcardgen = vcardgen.main:main'],
    },
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        #'Development Status :: 1 - Planning',
        #'Development Status :: 2 - Pre-Alpha',
        #'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        #'Development Status :: 5 - Production/Stable',
        #'Development Status :: 6 - Mature',
        #'Development Status :: 7 - Inactive',
        'Intended Audience :: System Administrators',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: German',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
    ]
)