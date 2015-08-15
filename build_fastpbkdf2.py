from __future__ import absolute_import, division, print_function

import os
import sys

from cffi import FFI

DIR = os.path.join(os.path.dirname(__file__), "src")

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
    "fastpbkdf2",
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
