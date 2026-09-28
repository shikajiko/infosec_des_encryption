from .tables import PC1, PC2, SHIFTS
from .utils import permute, rotate_left

def generate_round_keys(key_bits: str) -> list[str]:
    key56 = permute(key_bits, PC1)
    C, D = key56[:28], key56[28:]

    round_keys = []
    for shift in SHIFTS:
        C = rotate_left(C, shift)   
        D = rotate_left(D, shift)
        round_keys.append(permute(C + D, PC2))
    return round_keys