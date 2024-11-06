import qrcode as qr
qrcode = qr.make("https://chat.openai.com/")
qrcode.save("ChatGpt.jpg")