import qrcode

img = qrcode.make("www.mps.co.at")
img.save("mps.png")