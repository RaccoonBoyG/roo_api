#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C0111,W6005,W6100
from __future__ import absolute_import, print_function

import os
import re
import sys

from setuptools import setup


def get_version(*file_paths):
    """
    Extract the version string from the file at the given relative path fragments.
    """
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


VERSION = get_version('roo_api', '__init__.py')

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (VERSION, VERSION))
    os.system("git push --tags")
    sys.exit()

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
CHANGELOG = open(os.path.join(os.path.dirname(__file__), 'CHANGELOG.rst')).read()
LICENSE = open(os.path.join(os.path.dirname(__file__), 'LICENSE')).read()

setup(
    name='roo_api',
    version=VERSION,
    description='API for transferring data to a "Single Window Resource"',
    long_description=README + '\n\n' + CHANGELOG + '\n\n' + LICENSE,
    author='N.V.Ignatchenko, D.S.Vesloguzov, A.F.Galimzyanov',
    author_email='mastergowen@gmail.com, vesloguzov@gmail.com, alexofficialkek@gmail.com',
    url='https://github.com/RaccoonBoyG/roo_api.git,
    license="MIT",
    zip_safe=False,
    keywords='Django edx',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        #'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    packages=[
        'roo_api',
    ],
    include_package_data=True,
    install_requires=[
        "Django>=1.8,<2.0",
        "django-model-utils>=2.3.1",
        "djangorestframework>=3.1,<3.7",
        "django-ipware>=1.1.0",
        "edx-opaque-keys>=0.4",
        "pytz>=2016",
        "pycryptodomex>=3.4.7",
        "python-dateutil>=2.1",
        "requests",
        "six",
    ],
    dependency_links=[]
)