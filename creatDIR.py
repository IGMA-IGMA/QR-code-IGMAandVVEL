import os
import shutil


def creat_DIR():
    if not os.path.isdir("imagesQR"):
        os.mkdir('imagesQR')
        os.mkdir('imagesQR/images_save')
        os.mkdir('imagesQR/images_open')


def delit_DIR():
    shutil.rmtree('imagesQR')
