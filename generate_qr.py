import qrcode
from PIL import Image

# Website URL
website_url = "https://carlogregore01.github.io/Resume/"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(website_url)
qr.make(fit=True)

# Create the QR code image - Black and White
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code
img.save('static/images/contact_qr.png')
print('QR code updated to website URL (Black/White) successfully!')
