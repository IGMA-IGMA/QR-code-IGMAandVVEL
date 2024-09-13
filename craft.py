import qrcode
import cv2
import os
import os.path


def creating_QR_code(link: str, where: str):
    if where == "w":
        if len(link) == 0 or link == " ":
            print("Переданно пустое значение")
            return "site_images/ErrorGenerate.png", "Generate Error"

        l = len(os.listdir("static/imagesQR/images_save"))

        img = qrcode.make(link)
        img.save(f"static/imagesQR/images_save/{l + 1}.png")
        try:
            print("Успешно")
            return f"imagesQR/images_save/{l + 1}.png", "Успешно"
        except:
            return "site_images/ErrorGenerate.png", "Generate Error"

    if where == "t":
        l = len(os.listdir("telega_db/imagesQR/images_save"))
        img = qrcode.make(link)
        img.save(f"telega_db/imagesQR/images_save/{l + 1}.png")
        return f"telega_db/imagesQR/images_save/{l + 1}.png"


def recognize_qr_code_and_print_link(image_path: str):

    img = cv2.imread(image_path)

    qr_code_detector = cv2.QRCodeDetector()

    data, bbox, _ = qr_code_detector.detectAndDecode(img)

    if data:
        return data, True
    else:
        return "QR-code not found", False
