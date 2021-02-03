#!/usr/bin/env python3
#
import sys

from setuptools import setup, find_packages

__author__ = "Fred C. (W6BSD)"
__version__ = '0.1.5'
__license__ = 'BSD'

py_version = sys.version_info[:2]
if py_version < (3, 5):
  raise RuntimeError('Randwire requires Python 3.5 or later')

def readme():
  with open('README.md') as fd:
    return fd.read()

setup(
  name='randwire',
  version=__version__,
  description='Random Length Antenna Calculator',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/0x9900/randwire/',
  license=__license__,
  author=__author__,
  author_email='w6bsd@bsdworld.org',
  py_modules=['randwire'],
  install_requires=['matplotlib'],
  entry_points = {
    'console_scripts': ['randwire = randwire:main'],
  },
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Telecommunications Industry',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Topic :: Communications :: Ham Radio',
  ],
)
