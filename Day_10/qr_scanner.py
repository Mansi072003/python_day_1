import qrcode

img = qrcode.make('Hello, Mansi!')
img.show()  
img.save("hello_qr.png")  