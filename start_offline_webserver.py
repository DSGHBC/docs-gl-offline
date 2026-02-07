import http.server
import socketserver
import argparse
import os
import socket

os.chdir('htdocs')

class Handler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map, '': 'text/html'}

def is_port_in_use(port: int,host: str="localhost")->bool:
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.settimeout(1)
        return s.connect_ex((host,port))==0

def find_available_port(start_port: int = 8000,host: str = "localhost")->int:
    port = start_port
    while port <= 65535:
        if not is_port_in_use(port,host):
            return port
        port += 1
    raise RuntimeError("No avilable ports found (1024-65535)")

def main():
    parser = argparse.ArgumentParser(
        description='Local server for docs.gl offline version',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        '--port',
        type=int,
        default=8000,
        help='Port number to run the local server (1024 - 65535)',
        choices=range(1024,65536)
    )

    args=parser.parse_args()

    host = "localhost"
    port = args.port 

    if is_port_in_use(port,host):
        print(f"\033[31m[ERROR]: Port {port} is already in use!\033[0m")

        try:
            port=find_available_port(port+1)
            print(f"\033[32mSuggested available port: {port} (run with --port {port})\033[0m")
        except RuntimeError:
            print(f"\033[31mNo available ports found in range 1024-65535")
        return

    try: 
        with socketserver.ThreadingTCPServer((host, port), Handler) as httpd:
            httpd.request_queue_size = 10
            print(f"\033[32mServer started successfully!\033[0m\nServing docs at http://{host}:{port}")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\033[31m\nServer stopped.\033[0m")
        httpd.server_close()
    except Exception as e:
        print(f"\033[31mServer failed to start: {str(e)}\033[0m")

if __name__ =='__main__':
    main()