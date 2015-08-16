from __future__ import absolute_import, division, print_function

from fastpbkdf2._fastpbkdf2 import ffi, lib


def pbkdf2_hmac(name, password, salt, rounds, dklen=None):
    if name not in ["sha1", "sha256", "sha512"]:
        raise ValueError("unsupported hash type")

    algorithm = {
        "sha1": (lib.fastpbkdf2_hmac_sha1, 20),
        "sha256": (lib.fastpbkdf2_hmac_sha256, 32),
        "sha512": (lib.fastpbkdf2_hmac_sha512, 64),
    }

    out_length = dklen or algorithm[name][1]
    out = ffi.new("uint8_t[]", out_length)
    algorithm[name][0](
        password, len(password),
        salt, len(salt),
        rounds,
        out, out_length
    )

    return ffi.buffer(out)[:]
