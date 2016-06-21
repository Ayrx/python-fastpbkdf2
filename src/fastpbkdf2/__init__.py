# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import absolute_import, division, print_function

from fastpbkdf2._fastpbkdf2 import ffi, lib


FASTPBKDF2_GIT_HASH = "6442ac9"
algorithm = {
    "sha1": (lib.fastpbkdf2_hmac_sha1, 20),
    "sha256": (lib.fastpbkdf2_hmac_sha256, 32),
    "sha512": (lib.fastpbkdf2_hmac_sha512, 64),
}


def pbkdf2_hmac(name, password, salt, rounds, dklen=None):
    if name not in ["sha1", "sha256", "sha512"]:
        raise ValueError("unsupported hash type")

    out_length = dklen or algorithm[name][1]
    out = ffi.new("uint8_t[]", out_length)
    algorithm[name][0](
        password, len(password),
        salt, len(salt),
        rounds,
        out, out_length
    )

    return ffi.buffer(out)[:]
