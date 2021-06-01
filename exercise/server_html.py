import socket
import time

class app:
    def __init__(self):
        self.server = socket.socket()
        self.HOST = socket.gethostbyname(socket.gethostname())
        self.HOST = '127.0.0.1'
        self.PORT = 1234
        self.ADDR = (self.HOST, self.PORT)
        self.server.bind(self.ADDR)
        
    def route(self, path):
        def wrapper(func):
            webpage = func()
            self.resp =\
f"""HTTP/1.1 200 OK
Date:{time.time()}
Content-Length: {len(webpage)}
Content-Type: text/html

{webpage}"""
        return wrapper

    def run(self):
        print(f"\n[STARTED] Service has been started.")  
        self.server.listen()
        print(f"[LISTENING] Started listening on https://{self.HOST}:{self.PORT}")  
        #time.sleep(2)
        for i in range(5):  
            conn, addr = self.server.accept()
            conn.recv(1024)
            conn.send(self.resp.encode())
            conn.close()
            print("[HIT]")
        self.server.close()
