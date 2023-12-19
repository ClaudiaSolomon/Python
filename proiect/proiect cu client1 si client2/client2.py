import socket

s = socket.socket()

port = 12345
s.connect(('127.0.0.1', port))
s.send('client2'.encode())
try:
    while True:
        receive=s.recv(1024).decode()
        print(receive)
        if "won" in receive or "lost" in receive:
            break
        if "Welcome" in receive:
            value="jhdjsdjhk"
        else:
            value = input()
        s.send(value.encode())
        if value.lower() == "exit":
            break

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    s.close()
