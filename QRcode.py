import qrcode
import cv2

# QR Code Generator
def generate_qr(data, filename):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)
    print(f"QR code saved as {filename}")

# QR Code Decoder
def decode_qr(filename):
    img = cv2.imread(filename)
    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(img)
    return data if data else "No data found."

# Example
data = input("Enter data to encode in QR: ")
filename = "qrcode.png"
generate_qr(data, filename)
print("Decoded data:", decode_qr(filename))
