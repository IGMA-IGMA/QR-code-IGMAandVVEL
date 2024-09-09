import os
import shutil


def creat_DIR():
    if not os.path.isdir("static/imagesQR"):
        os.mkdir('static/imagesQR')
        os.mkdir('static/imagesQR/images_save')
        os.mkdir('static/imagesQR/images_open')


def delit_DIR():
    if os.path.isdir("static/imagesQR"):
        shutil.rmtree('static/imagesQR')
