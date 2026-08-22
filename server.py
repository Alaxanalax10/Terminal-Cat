import socket
import threading

# --- FLYNETX THEME COLORS ---
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Server Configuration
HOST = '127.0.0.1' 
PORT = 65432       

clients = []
aliases = []

def broadcast(message):
    """Broadcasts encrypted packets to all connected Terminal Cat clients."""
    for client in clients:
        try:
            client.send(message)
        except:
            pass

def handle_client(client):
    """Monitors the neural link of a specific user."""
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            if client in clients:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                alias = aliases[index]
                disconnect_msg = f"{CYAN}[FlyNetX SYSTEM] {alias} severed their link.{RESET}"
                broadcast(disconnect_msg.encode('utf-8'))
                print(disconnect_msg)
                aliases.remove(alias)
            break

def start_server():
    """Initializes the FlyNetX mainframe."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    
    print(f"{CYAN}{BOLD}")
    print("  ___ _       _  _     _  __  __ ")
    print(" | __| |_ _ _| \| |___| |_\ \/ / ")
    print(" | _|| | || | .` / -_)  _|>  <   ")
    print(" |_| |_|\_, |_|\_\___|\__/_/\_\  ")
    print("        |__/                     ")
    print("========================================")
    print("      T E R M I N A L   C A T           ")
    print("========================================")
    print(f"[FlyNetX SYSTEM] Mainframe online on port {PORT}. Awaiting connections...{RESET}")

    while True:
        client, address = server.accept()
        print(f"{CYAN}[FlyNetX SYSTEM] Incoming connection from {str(address)}{RESET}")

        client.send('ALIAS'.encode('utf-8'))
        alias = client.recv(1024).decode('utf-8')
        aliases.append(alias)
        clients.append(client)

        print(f"{CYAN}[FlyNetX SYSTEM] Agent registered: {alias}{RESET}")
        broadcast(f"{CYAN}[FlyNetX SYSTEM] {alias} jacked into Terminal Cat.{RESET}".encode('utf-8'))
        client.send(f"{CYAN}[FlyNetX SYSTEM] Link established. Welcome to Terminal Cat.{RESET}".encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    start_server()