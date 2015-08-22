python-fastpbkdf2
===========

[![Build Status](https://travis-ci.org/Ayrx/python-fastpbkdf2.svg?branch=master)](https://travis-ci.org/Ayrx/python-fastpbkdf2)
[![codecov.io](http://codecov.io/github/Ayrx/python-fastpbkdf2/coverage.svg?branch=master)](http://codecov.io/github/Ayrx/python-fastpbkdf2?branch=master)

python-fastpbkdf2 is a set of Python bindings for
[fastpbkdf2](https://github.com/ctz/fastpbkdf2) with an interface compatible
with the standard library's `hashlib.pbkdf2_hmac`. Initial testing shows that
it is about 40% faster than the standard library implementation.

python-fastpbkdf2 supports and is tested against Python versions 2.7, 3.3, 3.4.

# License

python-fastpbkdf2 is made available under both the BSD and Apache Software
License Version 2.0 licenses. See the `LICENSE.BSD` and `LICENSE.APACHE` files
for the exact terms of the license.

# Bug reports, security issues and contributing

python-fastpbkdf2 welcomes any bug reports, fixes and suggestions. If an issue
is security-sensitive, please email me directly at terrycwk1994@gmail.com.

If contributing a patch, please adhere to the following guidelines:

* Follow PEP 8. The test suite runs a flake8 lint to catch any issues.
* Keep patches small to ease the review process. Bigger patches can be broken
  up in logical chunks.
* Ensure that test coverage remains at 100%.
