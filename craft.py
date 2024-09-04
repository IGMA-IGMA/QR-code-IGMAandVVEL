import qrcode
import os
import cv2
from pyzbar.pyzbar import decode
import os.path


def creating_QR_code(link: str):

    if len(link) == 0 or link == ' ':
        print('Переданно пустое значение')
        return 'SaveError'

    l = len(os.listdir('image_save'))

    img = qrcode.make(link)
    img.save(f'image_save/{l + 1}.png')
    try:
        print('Успешно')
        return 'ImageSave'
    except:
        return 'SaveError'


def recognize_qr_code_and_print_link(image_path: str):

    if not os.path.exists(image_path):
        print('Image not found in directoru')
        return 0
    # Читаем изображение с QR-кодом
    image = cv2.imread(image_path)

    # Распознаем QR-код на изображении
    qr_codes = decode(image)

    # Проверяем, найден ли QR-код
    if qr_codes:
        for qr_code in qr_codes:
            # Получаем данные из QR-кода
            qr_data = qr_code.data.decode('utf-8')
            print(f"Распознанная ссылка: {qr_data}")
            return qr_data
    else:
        print("QR-код не найден.")
        return 'QR-code not founded'


recognize_qr_code_and_print_link('image_save/img.png')