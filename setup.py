# -*- coding: utf8 -*-
from __future__ import unicode_literals
from distutils.core import setup

import os


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except:
        return ''


setup(
    name='django-webodt',
    version='0.4.0',
    author='NetAngels',
    author_email='info@netangels.ru',
    packages=['webodt', 'webodt.converters', 'webodt.tests'],
    url='https://github.com/fazafantast/django-webodt',
    license='BSD License',
    description=u'ODF template handler and odt to html, pdf, doc, etc converter',
    long_description=read('README.rst'),
    install_requires=[
        'Django',
        'lxml',
    ],
    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)
