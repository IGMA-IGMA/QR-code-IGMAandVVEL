import qrcode
import os

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
def creating_QR_code(link: str, where: str, COLOR="black", BACKCOLOR="white"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color=COLOR, back_color=BACKCOLOR)


    if where == "w":
        if len(link) == 0 or link == " ":
            print("Переданно пустое значение")
            return "site_images/ErrorGenerate.png", "Generate Error"

        l = len(os.listdir("static/imagesQR/images_save"))

        img.save(f"static/imagesQR/images_save/{l + 1}.png")
        try:
            print("Успешно")
            return f"imagesQR/images_save/{l + 1}.png", "Успешно"
        except:
            return "site_images/ErrorGenerate.png", "Generate Error"

    if where == "t":
        l = len(os.listdir("telega_db/imagesQR/images_save"))
        img.save(f"telega_db/imagesQR/images_save/{l + 1}.png")
        return f"telega_db/imagesQR/images_save/{l + 1}.png"
