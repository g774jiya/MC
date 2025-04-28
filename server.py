import socket

# Set up IP address and port
IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

def main():
    print("[STARTING] Server is starting...")

    # Create server socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print("[LISTENING] Server is listening...")

    while True:
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")

        # Step 1: Receive filename
        filename = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving the filename: {filename}")
        conn.send("Filename received.".encode(FORMAT))

        # Step 2: Receive file data
        with open(f"Received_{filename}", "w") as file:
            data = conn.recv(SIZE).decode(FORMAT)
            file.write(data)

        conn.send("Data received.".encode(FORMAT))
        print(f"[FILE RECEIVED] File {filename} received from {addr}.")

        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected.")

if __name__ == "__main__":
    main()
