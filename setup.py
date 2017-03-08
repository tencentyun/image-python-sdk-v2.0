#!/usr/bin/env python
# coding=utf-8

import re
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

version = '2.0.1'
with open('qcloud_image/__init__.py', 'r') as fd:
    match = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE)
    if match:
        version = match.group(1)
if not version:
    raise Exception('Cannot find version')

setup(
    name='qcloud_image',
    version=version,
    keywords = ('qcloud', 'image'),
    author='serenazhao',
    author_email='serenazhao@tencent.com',
    url='https://github.com/tencentyun/image-python-sdk-v2.0',
    description='Python 2/3 SDK for tencent qcloud image',
    license='MIT',
    packages=find_packages()
    )
