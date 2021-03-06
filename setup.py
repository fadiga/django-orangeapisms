#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu

""" Allow any django app to handle SMS-MO, SMS-MT using the Orange API. """

from codecs import open

from setuptools import setup, find_packages

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='orangeapisms',
    version='0.18',
    description='Django app to add support for Orange API SMS-MO, SMS-MT',
    long_description=readme,
    author='renaud gaudin',
    author_email='rgaudin@gmail.com',
    url='http://github.com/rgaudin/django-orangeapisms',
    packages=find_packages('.'),
    zip_safe=False,
    platforms='any',
    include_package_data=True,
    package_data={'': ['README.rst', 'LICENSE']},
    package_dir={'orangeapisms': 'orangeapisms'},
    install_requires=[
        'Django >= 1.8.5',
        'django-forms-bootstrap >= 3.0.1',
        'iso8601 >= 0.1.10',
        'pytz >= 2015.6',
        'requests >= 2.8.1',
        'simplejson >= 3.8.2',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
    ]
)
