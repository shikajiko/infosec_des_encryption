import socket
import config
from network.chat import run_chat

s = socket.socket()
s.connect((config.HOST, config.PORT))
print(f"Connected to {config.HOST}:{config.PORT}")
run_chat(s, "CLIENT")

