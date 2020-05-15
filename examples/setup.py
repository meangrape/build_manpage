#!/usr/bin/env python3

import os.path
import sys

from setuptools import setup, find_packages
from build_manpage import build_manpage

HOME=os.path.expanduser('~')

setup(
    name='example',
    version='0.2.0',
    author='Jay Edwards',
    cmdclass={'build_manpage': build_manpage},
    author_email='jay@meangrape.com',
    data_files=[('%s/share/man/man1' % sys.prefix, ['doc/example.1'])],
    license='Apache License 2.0',
    description='build_manpage example',
    long_description=open('../README').read(),
    entry_points = {
        'console_scripts': [
            'example = example.example:main',
        ],
        'distutils.commands': [
            'build_manpage = build_manpage.build_manpage'
        ]
    }
)
