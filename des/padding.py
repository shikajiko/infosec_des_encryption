def pad(data: bytes, block_size: int = 8) -> bytes:
    n = block_size - (len(data) % block_size)
    return data + bytes([n]) * n

def unpad(data: bytes, block_size: int = 8) -> bytes:
    if not data or len(data) % block_size != 0:
        raise ValueError("invalid padded data length")
    n = data[-1]
    if n < 1 or n > block_size or data[-n:] != bytes([n]) * n:
        raise ValueError("invalid padding (wrong key or corrupted data?)")
    return data[:-n]