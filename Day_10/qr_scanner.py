import qrcode

img = qrcode.make('Hello, Mansi!')
img.show()  
img.save("hello_qr.png")  


import cv2
from pyzbar.pyzbar import decode

img = cv2.imread('hello_qr.png')


decoded_objects = decode(img)


for obj in decoded_objects:
    print("QR Code Data:", obj.data.decode('utf-8'))
