import qrcode

try:
    qr = qrcode.QRCode(version=1, box_size=20, border=20, error_correction=qrcode.constants.ERROR_CORRECT_H)
    data = input("Enter LINK or any text to convert it into qr code: ")
    qr.add_data(data)
    qr.make(fit=True)
    qrcode_color = input("Enter the color of qrcode: ")
    Background_color = input("Enter the background_color of qrcode: ")
    image = qr.make_image(fill_color=qrcode_color.strip(), back_color=Background_color.strip())
    print("Making Qr Code For you.......")
    image_name = "Red QRcode.jpg"
    image.save(image_name)
    print("Finished.")
except Exception as e:
    print(f"An error occurred: {e}")
