import qrcode
import os
import os.path


def creating_QR_code(link: str):

    if len(link) == 0 or link == ' ':
        print('Переданно пустое значение')
        return 'site_images/ErrorGenerate.png', 'Generate Error'

    l = len(os.listdir('static/imagesQR/images_save'))

    img = qrcode.make(link)
    img.save(f'static/imagesQR/images_save/{l + 1}.png')
    try:
        print('Успешно')
        return f'imagesQR/images_save/{l + 1}.png', 'Успешно'
    except:
        return 'site_images/ErrorGenerate.png', 'Generate Error'


# def recognize_qr_code_and_print_link(image_path: str):
#

