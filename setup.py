#!/usr/bin/env python

import os
from setuptools import setup


# Requirements.
setup_requires = [
    'lowdown',
    'mock',
    'sphinx >= 1.3, < 2'
]

install_requires = []

# Readthedocs requires Sphinx extensions to be specified as part of
# install_requires in order to build properly.
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if on_rtd:
    install_requires.extend(setup_requires)

setup(name='Kraken Documentation',
      version='1.2.5',
      description='Kraken Rigging Framework Documentation',
      author='Eric Thivierge, Phil Taylor',
      author_email='ethivierge@gmail.com',
      url='http://fabric-engine.github.io/Kraken//',
      license='BSD 3-clause "New" or "Revised" License',
      setup_requires=setup_requires,
      install_requires=install_requires)
