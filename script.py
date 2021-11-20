from pyzbar.pyzbar import decode
from PIL import Image
import pyqrcode
url = pyqrcode.create("https://the-morpheus.de", error='H', )
url.png("PNG\qrcode2.png", scale=5)

# decode
from PIL import 
data = decode(Image.open("PNG\qrcode.png"))
print(data)
