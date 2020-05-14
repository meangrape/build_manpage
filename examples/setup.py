import sys

from setuptools import setup, find_packages
from build_manpage import build_manpage

setup(
    cmdclass={'build_manpage': build_manpage},
    data_files=[('%s/share/man/man1' % sys.prefix, ['doc/example.1'])],
    setup_requires=[
       "github-distutils >= 0.1.0",
       ],
    entry_points = {
        'distutils.commands': [
            'build_manpage = build_manpage.build_manpage'
        ]
    }
)
