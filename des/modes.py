import os
from .core import encrypt_block, decrypt_block
from .padding import pad, unpad
from .utils import xor_bytes

BLOCK = 8

def _check_key(key: bytes):
    if len(key) != 8:
        raise ValueError("DES key must be exactly 8 bytes")

def encrypt(plaintext: bytes, key: bytes, mode: str = "CBC") -> bytes:
    _check_key(key)
    data = pad(plaintext)
    blocks = [data[i:i + BLOCK] for i in range(0, len(data), BLOCK)]

    if mode == "ECB":
        return b"".join(encrypt_block(b, key) for b in blocks)

    if mode == "CBC":
        iv = os.urandom(BLOCK)            
        prev, out = iv, [iv]              
        for b in blocks:
            prev = encrypt_block(xor_bytes(b, prev), key)
            out.append(prev)
        return b"".join(out)

    raise ValueError(f"unknown mode: {mode}")

def decrypt(ciphertext: bytes, key: bytes, mode: str = "CBC") -> bytes:
    _check_key(key)

    if mode == "ECB":
        blocks = [ciphertext[i:i + BLOCK] for i in range(0, len(ciphertext), BLOCK)]
        return unpad(b"".join(decrypt_block(b, key) for b in blocks))

    if mode == "CBC":
        iv, body = ciphertext[:BLOCK], ciphertext[BLOCK:]
        blocks = [body[i:i + BLOCK] for i in range(0, len(body), BLOCK)]
        prev, out = iv, []
        for b in blocks:
            out.append(xor_bytes(decrypt_block(b, key), prev))
            prev = b
        return unpad(b"".join(out))

    raise ValueError(f"unknown mode: {mode}")