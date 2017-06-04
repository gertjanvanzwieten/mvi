#! /usr/bin/env python3

import setuptools

setuptools.setup(
  name='mvi',
  version='0.9',
  author='Gertjan van Zwieten',
  py_modules=['mvi'],
  entry_points={'console_scripts': ['mvi=mvi:cli']},
)
