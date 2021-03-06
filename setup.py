#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = '0.1.14'

if sys.argv[-1] == 'publish':
    try:
        import wheel
        print(("Wheel version: ", wheel.__version__))
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on git:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = ''
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-fine-uploader-s3',
    version=version,
    description="""Your project description goes here""",
    long_description=readme + '\n\n' + history,
    author='Aneesh Kumar',
    author_email='aneesh@cybereyelabs.io',
    url='https://github.com/anush0247/django-fine-uploader-s3',
    packages=[
        'django_fine_uploader_s3',
    ],
    include_package_data=True,
    install_requires=[],
    license="MIT",
    zip_safe=False,
    keywords='django-fine-uploader-s3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
