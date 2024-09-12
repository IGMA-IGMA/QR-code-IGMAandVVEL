from pyzbar.pyzbar import decode
from PIL import Image


def find_qr_codes(image_path):
    # Загружаем изображение
    image = Image.open(image_path)

    # Декодируем QR-коды на изображении
    qr_codes = decode(image)

    if not qr_codes:
        print("QR-коды не найдены.")
        return

    # Обрабатываем каждый найденный QR-код
    for qr_code in qr_codes:
        # Получаем данные QR-кода
        qr_data = qr_code.data.decode('utf-8')
        print(f"QR-код найден! Данные: {qr_data}")


# Пример использования
find_qr_codes('1.png')
