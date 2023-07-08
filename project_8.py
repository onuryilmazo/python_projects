import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://www.youtube.com/watch?v=Y3Wm9OlBRYs&t=96s&ab_channel=hulusi%C3%B6zbilgin"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.svg("aminadakoydugum.svg", scale = 8) 