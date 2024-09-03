import qrcode

def creating_QR_code(link: str):

    img = qrcode.make(link, box_size=50)
    img.save('hello.png')
    print(True)
