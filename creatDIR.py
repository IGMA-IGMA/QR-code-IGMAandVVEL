import os
import shutil


def creat_DIR_site():
    if not os.path.isdir("static/imagesQR"):
        os.mkdir('static/imagesQR')
        os.mkdir('static/imagesQR/images_save')
        os.mkdir('static/imagesQR/images_open')


def delit_DIR_site():
    if os.path.isdir("static/imagesQR"):
        shutil.rmtree('static/imagesQR')


def creat_DIR_telega():
    if not os.path.isdir("telega_db"):
        os.mkdir('telega_db')
        os.mkdir('telega_db/imagesQR')
        os.mkdir('telega_db/imagesQR/images_save')
        os.mkdir('telega_db/imagesQR/images_open')
        print('TELEGRAM db created')


def delit_DIR_telega():
    if os.path.isdir("telega_db"):
        shutil.rmtree('telega_db')
        print('TELEGRAM db del')

#ADMIN ROOT
def clean_directory(directory_path):
    perechisl = ''
    # Проходим по содержимому директории
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        # Удаляем файлы
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
            perechisl += f'\t{file_path}'

            print(f"Файл {file_path} удален.")
    return perechisl

