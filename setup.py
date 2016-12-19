#! /usr/bin/env python
#
# Copyright (C) 2016 Ulrich Feindt

DESCRIPTION = "TBA"
LONG_DESCRIPTION = """TBA"""

DISTNAME = 'lcfitter'
AUTHOR = 'Ulrich Feindt'
MAINTAINER = 'Ulrich Feindt' 
MAINTAINER_EMAIL = 'ulrich.feindt@fysik.su.se'
URL = 'https://github.com/ufeindt/lcfitter/'
LICENSE = 'BSD (3-clause)'
DOWNLOAD_URL = 'https://github.com/ufeint/lcfitter/tarball/0.1.0'
VERSION = '0.1.0'

try:
    from setuptools import setup, find_packages
    _has_setuptools = True
except ImportError:
    from distutils.core import setup

if __name__ == "__main__":
    if _has_setuptools:
        packages = find_packages()
    else:
        # This should be updated if new submodules are added
        packages = ['lcfitter']

    setup(name=DISTNAME,
          author=AUTHOR,
          author_email=MAINTAINER_EMAIL,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          long_description=LONG_DESCRIPTION,
          license=LICENSE,
          url=URL,
          version=VERSION,
          download_url=DOWNLOAD_URL,
          packages=packages,
          classifiers=[
              'Intended Audience :: Science/Research',
              'Programming Language :: Python :: 2.7',
              'License :: OSI Approved :: BSD License',
              'Topic :: Scientific/Engineering :: Astronomy',
              'Operating System :: POSIX',
              'Operating System :: Unix',
              'Operating System :: MacOS'],
          install_requires=[
              'propobject>=0.1.0',
              'astropy>=1.2.1',
              'sncosmo>=1.3.1'],
    )
