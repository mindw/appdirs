#!/usr/bin/env python
from sys import version_info as v
if any([v < (2, 7), (3,) < v < (3, 4)]):
    raise Exception("Unsupported Python version %d.%d. Requires Python >= 2.7 "
                    "or >= 3.4." % v[:2])

import os
import os.path
from setuptools import setup


def get_version():
    with open('appdirs.py') as fp:
        _locals = {}
        for line in fp:
            if line.startswith('__version__'):
                exec (line, None, _locals)
                return _locals['__version__']


def read(fname):
    inf = open(os.path.join(os.path.dirname(__file__), fname))
    out = "\n" + inf.read().replace("\r\n", "\n")
    inf.close()
    return out


setup(
    name='appdirs',
    version=get_version(),
    description='A small Python module for determining appropriate " + \
        "platform-specific dirs, e.g. a "user data dir".',
    long_description=read('README.rst') + '\n' + read('CHANGES.rst'),
    classifiers=[c.strip() for c in """
        Development Status :: 4 - Beta
        Intended Audience :: Developers
        License :: OSI Approved :: MIT License
        Operating System :: OS Independent
        Programming Language :: Python :: 2
        Programming Language :: Python :: 2.7
        Programming Language :: Python :: 3
        Programming Language :: Python :: 3.4
        Programming Language :: Python :: 3.5
        Programming Language :: Python :: Implementation :: PyPy
        Programming Language :: Python :: Implementation :: CPython
        Topic :: Software Development :: Libraries :: Python Modules
        """.split('\n') if c.strip()],
    test_suite='test.test_api',
    tests_require=[],
    keywords='application directory log cache user',
    author='Trent Mick',
    author_email='trentm@gmail.com',
    maintainer='Trent Mick; Sridhar Ratnakumar',
    maintainer_email='trentm@gmail.com; github@srid.name',
    url='http://github.com/ActiveState/appdirs',
    license='MIT',
    py_modules=["appdirs"],
)
