#!/usr/bin/bash

echo "Benchmark hashlib..."
python -m timeit -n 100 -s "from hashlib import pbkdf2_hmac" "pbkdf2_hmac('sha1', b'password', b'salt', 100000)"

echo "Benchmark fastpbkdf2..."
python -m timeit -n 100 -s "from fastpbkdf2 import pbkdf2_hmac" "pbkdf2_hmac('sha1', b'password', b'salt', 100000)"
