from .tables import IP, FP, E, P, S_BOXES
from .utils import permute, xor, bytes_to_bits, bits_to_bytes
from .key_schedule import generate_round_keys

def f(R: str, K: str) -> str:
    expanded = permute(R, E)              
    mixed = xor(expanded, K)              

    out = ""
    for i in range(8):
        chunk = mixed[i * 6:(i + 1) * 6]
        row = int(chunk[0] + chunk[5], 2)
        col = int(chunk[1:5], 2)
        out += f"{S_BOXES[i][row][col]:04b}"   

    return permute(out, P)

def _process_block(block_bits: str, round_keys: list[str]) -> str:
    block_bits = permute(block_bits, IP)
    L, R = block_bits[:32], block_bits[32:]

    for K in round_keys:
        L, R = R, xor(L, f(R, K))

    return permute(R + L, FP)             

def encrypt_block(block: bytes, key: bytes) -> bytes:
    keys = generate_round_keys(bytes_to_bits(key))
    return bits_to_bytes(_process_block(bytes_to_bits(block), keys))

def decrypt_block(block: bytes, key: bytes) -> bytes:
    keys = generate_round_keys(bytes_to_bits(key))
    return bits_to_bytes(_process_block(bytes_to_bits(block), keys[::-1]))