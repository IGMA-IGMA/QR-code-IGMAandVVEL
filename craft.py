import qrcode
import sys


def creating_QR_code(link: str):
    img = qrcode.make(link)
    img.save('image_save/hello.png')
    try:
        return 1
    except:
        return 0


def recognition_QR_code(img):
    d = qrcode.Decoder()
    if d.decode('hello.png'):
        print
        'result: ' + d.result
    else:
        print
        'error: ' + d.error


creating_QR_code('https://stackoverflow.com/questions/44699682/how-to-save-a-file-to-a-specific-directory-in-python')
