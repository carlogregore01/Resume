import qrcode
from PIL import Image

# Create vCard format for contact information
vcard_data = """BEGIN:VCARD
VERSION:3.0
FN:Carlo Gregore
TEL:09175167110
EMAIL:carlogregore01@gmail.com
URL:https://carlogregore01.github.io/Resume/
END:VCARD"""

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(vcard_data)
qr.make(fit=True)

# Create the QR code image
img = qr.make_image(fill_color="#F2AA4C", back_color="transparent")

# Save the QR code
img.save('static/images/contact_qr.png')
print('QR code generated successfully!')
