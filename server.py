import socket
from PIL import Image
from utils import recv_img

HOST = '127.0.0.1'
PORT = 50007

def server():
    p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    p.bind((HOST, PORT))
    p.listen(1)
    print("Server listening on {}:{}".format(HOST, PORT))
    conn, addr = p.accept()
    print("Connected by", addr)
    image = recv_img(conn)
    image.save('received_result.jpg')
    print("Image received and saved as received.jpg")
    conn.close()
    p.close()

if __name__ == "__main__":
    server()
