import socket 
import config 
from network.chat import run_chat

s = socket.socket() 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("0.0.0.0", config.PORT))
s.listen(1)
print(f"Server listening on port {config.PORT}")

conn, addr = s.accept()
print(f"Connected: {addr}")
run_chat(conn, "SERVER")
