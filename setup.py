#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import setup, find_packages


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


# Does not work with tox:
# install_requires = [
#     l for l in open(join(dirname(__file__), 'requirements.txt')).read().split('\n')
#     if l and not l.startswith('#')
# ]


setup(
    name             = 'sanic-secure-session',
    version          = '0.2.0',
    license          = 'MIT license',
    description      = 'A server-side secure sessions plugin for Sanic',
    long_description = '%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.md')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    author       = 'Sergei Beilin',
    author_email = 'saabeilin@gmail.com',
    url          = 'https://github.com/saabeilin/sanic-secure-session',
    # packages     = find_packages(),
    packages= find_packages('src'),
    # packages= ['sanic_secure_session'],
    package_dir  = {
        '': 'src',
    },
    # py_modules= [splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data = True,
    zip_safe             = False,
    classifiers          = [
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Utilities',
    ],
    keywords = [
        'sanic', 'session'
    ],
    install_requires = ['sanic', 'itsdangerous']
)
