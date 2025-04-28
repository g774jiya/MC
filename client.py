import socket

# Set up IP address and port
IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

def main():
    # Create client socket (IPv4, TCP)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    # Open the file to send
    file = open("Data/yt.txt", "r")
    data = file.read()

    # Step 1: Send the filename
    client.send("yt.txt".encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    # Step 2: Send the file data
    client.send(data.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    # Closing everything
    file.close()
    client.close()

if __name__ == "__main__":
    main()
