# -*- coding:utf-8 -*-

import os
import re

from setuptools import setup


def get_version(package):
    """
    Return package version as listed in `__version__` in `__init__.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


# package_name = 'timezonefinderL'
version = get_version('timezonefinderL')

with open('README.rst') as f:
    readme = f.read()

with open('CHANGELOG.rst') as changelog_file:
    changelog = changelog_file.read()

setup(
    name='timezonefinderL',
    version=version,
    packages=['timezonefinderL'],
    package_data={'timezonefinderL': ['poly_zone_ids.bin',
                                      'poly_coord_amount.bin',
                                      'poly_adr2data.bin',
                                      'poly_max_values.bin',
                                      'poly_data.bin',
                                      'poly_nr2zone_id.bin',
                                      'hole_poly_ids.bin',
                                      'hole_coord_amount.bin',
                                      'hole_adr2data.bin',
                                      'hole_data.bin',
                                      'shortcuts_entry_amount.bin',
                                      'shortcuts_adr2data.bin',
                                      'shortcuts_data.bin',
                                      'shortcuts_unique_id.bin', ]},
    description='Python library to look up timezone from coordinates offline. Light version of "timezonefinder".',
    author='J. Michelfeit',
    author_email='python@michelfe.it',
    license='MIT licence',
    url='https://github.com/MrMinimal64/timezonefinderL',  # use the URL to the github repo
    keywords='timezone coordinates latitude longitude location pytzwhere tzwhere',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Localization',
    ],
    long_description=readme + '\n\n' + changelog,
    install_requires=[
        'numpy',
    ],
)
