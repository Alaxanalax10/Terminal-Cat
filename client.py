import socket
import threading
import sys
import os

try:
    import colorama
    colorama.init()
except ImportError:
    pass 

# --- FLYNETX THEME COLORS ---
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

os.system('cls' if os.name == 'nt' else 'clear')

print(f"{CYAN}{BOLD}")
print("  ___ _       _  _     _  __  __ ")
print(" | __| |_ _ _| \| |___| |_\ \/ / ")
print(" | _|| | || | .` / -_)  _|>  <   ")
print(" |_| |_|\_, |_|\_\___|\__/_/\_\  ")
print("        |__/                     ")
print("========================================")
print("      T E R M I N A L   C A T           ")
print("========================================")
print(f"Connecting to FlyNetX servers... Done.{RESET}")

alias = input(f"{CYAN}Enter Agent Alias: {RESET}")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect(('127.0.0.1', 65432))
except Exception as e:
    print(f"{CYAN}[FATAL ERROR] FlyNetX Mainframe unreachable.{RESET}")
    sys.exit()

def receive_messages():
    """Listens for incoming broadcasts from FlyNetX."""
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'ALIAS':
                client.send(alias.encode('utf-8'))
            else:
                sys.stdout.write(f"\r\033[K{message}\n{CYAN}{alias} > {RESET}")
                sys.stdout.flush()
        except:
            print(f"\n{CYAN}[FlyNetX SYSTEM] Connection severed.{RESET}")
            client.close()
            break

def write_messages():
    """Transmits data to the FlyNetX mainframe."""
    while True:
        text = input(f"{CYAN}{alias} > {RESET}")
        
        if text.lower() == '/exit':
            print(f"{CYAN}[FlyNetX SYSTEM] Jacking out...{RESET}")
            client.close()
            sys.exit()
            
        message = f"{CYAN}[{alias}]{RESET} {CYAN}{text}{RESET}"
        client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.daemon = True
receive_thread.start()

write_thread = threading.Thread(target=write_messages)
write_thread.daemon = True
write_thread.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    print(f"\n{CYAN}[FlyNetX SYSTEM] Emergency disconnect.{RESET}")
    client.close()
    sys.exit()