def bytes_to_bits(data: bytes) -> str:
    return "".join(f"{b:08b}" for b  in data)

def bits_to_bytes(bits: str) -> bytes:
    return bytes(int(bits[i:i + 8], 2) for i in range(0, len(bits), 8))

def permute(bits: str, table) -> str:
    return "".join(bits[i-1] for i in table)

def xor(a: str, b: str) -> str:
    return "".join("0" if x == y else "1" for x, y in zip(a, b))

def rotate_left(bits: str, n: int) -> str:
    return bits[n:] + bits[:n]

def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))

