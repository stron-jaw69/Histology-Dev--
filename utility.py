import struct
import pickle

def send_img(sock, image):
    img_bytes = pickle.dumps(image)# get the length of the serialized image
    length = len(img_bytes)
    header = struct.pack('>I', length)
    sock.sendall(header)
    sock.sendall(img_bytes) #send the image bytes over the socket

def recv_img(sock):
    header = b''    # read 4 bytes from the socket to recieve the header
    while len(header) < 4:
        chunk = sock.recv(4 - len(header))
        if not chunk:
            raise ConnectionError('Socket closed before full header received')
        header += chunk
    data_len = struct.unpack('>I', header)[0]   #unpack the 4-byte header

    data = b''  # continue reading from the socket
    while len(data) < data_len:
        chunk = sock.recv(data_len - len(data)) #check if the connection is lost
        if not chunk:
            raise ConnectionError('Socket closed before full data received')
        data += chunk
      
    #deserialize the byte data back into the image object
    return pickle.loads(data)   
