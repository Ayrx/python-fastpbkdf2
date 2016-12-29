python-fastpbkdf2
===========

[![Build Status](https://travis-ci.org/Ayrx/python-fastpbkdf2.svg?branch=master)](https://travis-ci.org/Ayrx/python-fastpbkdf2)
[![codecov.io](http://codecov.io/github/Ayrx/python-fastpbkdf2/coverage.svg?branch=master)](http://codecov.io/github/Ayrx/python-fastpbkdf2?branch=master)

python-fastpbkdf2 is a set of Python bindings for
[fastpbkdf2](https://github.com/ctz/fastpbkdf2) with an interface compatible
with the standard library's `hashlib.pbkdf2_hmac`. Initial testing shows that
it is about 40% faster than the standard library implementation.

python-fastpbkdf2 supports and is tested against Python versions 2.7, 3.3, 3.4,
3.5, 3.6.

# Installation

python-fastpbkdf2 can be installed with pip:

```
pip install fastpbkdf2
```

python-fastpbkdf2 depends on CFFI to bind C code. `libffi-dev` and `python-dev`
may be required and can be installed with various package managers such as yum
or apt-get.

# How to use

python-fastpbkdf2 provides an interface compatible wtih
[`hashlib.pbkdf2_hmac`](https://docs.python.org/3/library/hashlib.html#hashlib.pbkdf2_hmac).
The module contains a single function that can be imported in place of
`hashlib.pbkdf2_hmac`.

```python
from fastpbkdf2 import pbkdf2_hmac
```

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
