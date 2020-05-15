NAME
====

example - build\_manpage example

SYNOPSIS
========

**example** usage: \[-h\] \[-i IAMID\] \[-v\]
{create,destroy,inventory,stop,license} \...

DESCRIPTION
===========

Based on blog post
https://andialbrecht.wordpress.com/2009/03/17/creating-a-man-page-with-distutils-and-optparse/
Latest original version (2017)
https://github.com/andialbrecht/build\_manpage

Should work on python3

This version works with argparse instead of optparse like the original
and doesn\'t require a separate step to build/install the man page

Look at setup.cfg and setup.py to see what you need to add to those
files.

It looks in setup.py to find information like authors &c. Look at
build\_manpage.py for details.

OPTIONS
=======

usage: example \[-h\] \[-i IAMID\] \[-v\]
{create,destroy,inventory,stop,license} \...

Manage EC2 example instances

positional arguments: {create,destroy,inventory,stop,license} create
Create a example group (instance, keypair, security group) destroy
Destroy a example group and associated resources inventory List examples
you have running in AWS stop Stop running instances license
http://github.com/meangrape/build\_manpage/LICENSE

optional arguments: -h, \--help show this help message and exit -i
IAMID, \--iam IAMID Your IAM id. We attempt to read an IAM\_ID
environemnt variable and fallback to your username. This is the primary
key used to identify AWS resources belonging to you (default: None) -v,
\--version show program\'s version number and exit

AUTHORS
=======

**example** was written by Jay Edwards \<jay\@meangrape.com\>.

DISTRIBUTION
============

The latest version of example may be downloaded from [](UNKNOWN)
