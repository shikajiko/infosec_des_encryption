import threading
from des import encrypt, decrypt
from network.framing import send_msg, recv_msg
import config

def run_chat(sock, name):
    threading.Thread(target=_receiver, args=(sock, name), daemon=True).start()
    _sender(sock, name)

def _sender(sock, name):
    while True:
        text = input()
        data = text.encode()
        if config.ENCRYPTION_ENABLED:
            data = encrypt(data, config.KEY, config.MODE)
        print(f"[{name}] sent (hex): {data.hex()}")
        send_msg(sock, data)

def _receiver(sock, name):
    while True:
        data = recv_msg(sock)
        if data is None:
            print(f"[{name}] connection closed")
            break
        print(f"[{name}] received (hex): {data.hex()}")
        if config.ENCRYPTION_ENABLED:
            data = decrypt(data, config.KEY, config.MODE)
        print(f'[{name}] plaintext: {data.decode(errors='replace')}')