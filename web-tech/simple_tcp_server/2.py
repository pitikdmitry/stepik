
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(11)

while True:
    conn, addr = s.accept()
    data = conn.recv(1024)
    conn.send(data)
    try:
        conn.close()
    except BaseException:
        pass
    