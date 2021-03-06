# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re, ast

# get version from __version__ variable in phtax/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('phtax/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
	name='phtax',
	version=version,
	description='Philippine Tax Module',
	author='JCB Digital Accounting',
	author_email='ask@jcbangquilcpa.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
)
