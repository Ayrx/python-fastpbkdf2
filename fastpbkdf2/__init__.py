from __future__ import absolute_import, division, print_function

from fastpbkdf2._fastpbkdf2 import ffi, lib


def pbkdf2_hmac(name, password, salt, rounds, dklen=None):
    if name not in ["sha1", "sha256", "sha512"]:
        return ValueError(
            "Algorithm {} not supported. "
            "Please use sha1, sha256 or sha512".format(name)
        )

    algorithm = {
        "sha1": (lib.fastpbkdf2_hmac_sha1, 20),
        "sha256": (lib.fastpbkdf2_hmac_sha256, 32),
        "sha512": (lib.fastpbkdf2_hmac_sha512, 64),
    }

    out = ffi.new("uint8_t[]", algorithm[name][1])
    algorithm[name][0](
        password, len(password),
        salt, len(salt),
        rounds,
        out, algorithm[name][1]
    )

    return ffi.string(out)
