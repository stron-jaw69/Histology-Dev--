from utils import send_img
from PIL import Image
import socket

HOST = '127.0.0.1'
PORT = 50007

def main():
    input_filename= "sample.jpg"
    image = Image.open(input_filename)
    p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    p.connect((HOST, PORT))
    send_img(p, image)
    print("Sample image sent")
    p.close()

if __name__ == "__main__":
    main()
