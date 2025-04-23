import qrcode

def generate_qr(data, filename):
    qr = qrcode.make(data)
    qr.show()
    qr.save(filename)
    print(f"QR Code saved as {filename}")

name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")

qr_data = f"{emp_id},{name}"
generate_qr(qr_data, f"{emp_id}_{name}.png")
