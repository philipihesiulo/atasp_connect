# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in atasp_connect/__init__.py
from atasp_connect import __version__ as version

setup(
	name='atasp_connect',
	version=version,
	description='Monitoring, evaluation and reporting tool for ATASP.',
	author='Philip Ihesiulo',
	author_email='philipihesiulo@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
