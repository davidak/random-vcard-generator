#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
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
    keywords=('random vcard generator test import export'),
    platforms='any',
    description=__doc__,
    long_description=codecs.open('README.rst', 'r', 'utf-8').read(),
    packages=['vcardgen'],
    entry_points = {
        'console_scripts': ['vcardgen = vcardgen.main:main'],
    },
    install_requires=[
        'PyZufall>=0.13.1',
        'frogress>=0.9.1',
        'argparse',
        'future'
    ],
    classifiers=[
        #'Development Status :: 1 - Planning',
        #'Development Status :: 2 - Pre-Alpha',
        #'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        #'Development Status :: 5 - Production/Stable',
        #'Development Status :: 6 - Mature',
        #'Development Status :: 7 - Inactive',
        #'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        #'Programming Language :: Python :: 3.0',
        #'Programming Language :: Python :: 3.1',
        #'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        #'Programming Language :: Python :: Implementation :: IronPython',
        #'Programming Language :: Python :: Implementation :: Jython',
        'Programming Language :: Python :: Implementation :: PyPy',
        #'Programming Language :: Python :: Implementation :: Stackless',
        'Intended Audience :: System Administrators',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: German',
        'Environment :: Console',
        'Operating System :: OS Independent',
    ]
)
