# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import absolute_import, division, print_function

import os

from cffi import FFI

DIR = os.path.join(os.path.dirname(__file__), "c")

ffi = FFI()
ffi.cdef(
    """
    void fastpbkdf2_hmac_sha1(const uint8_t *, size_t,
                              const uint8_t *, size_t,
                              uint32_t,
                              uint8_t *, size_t);

    void fastpbkdf2_hmac_sha256(const uint8_t *, size_t,
                                const uint8_t *, size_t,
                                uint32_t,
                                uint8_t *, size_t);

    void fastpbkdf2_hmac_sha512(const uint8_t *, size_t,
                                const uint8_t *, size_t,
                                uint32_t,
                                uint8_t *, size_t);
    """
)

ffi.set_source(
    "_fastpbkdf2",
    """
    #include "fastpbkdf2.h"
    """,
    sources=[
        os.path.join(DIR, "fastpbkdf2.c"),
    ],
    include_dirs=[DIR],
    libraries=["crypto"],
    extra_compile_args=[
        "-std=c99",
        "-O3",
        "-g",
    ]
)
