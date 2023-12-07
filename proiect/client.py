import socket

s = socket.socket()

port = 12345
s.connect(('127.0.0.1', port))

try:
    while True:
        receive=s.recv(1024).decode()
        print(receive)
        # if "You won!" in receive or "You lost!" in receive:
        #     break
        value = input()
        s.send(value.encode())
        if value.lower() == "exit":
            break

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    s.close()
