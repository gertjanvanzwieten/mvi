#! /usr/bin/env python3

import mvi, setuptools

setuptools.setup(
  name='mvi',
  version=mvi.__version__,
  author='Gertjan van Zwieten',
  py_modules=['mvi'],
  scripts=['mvi'],
)
