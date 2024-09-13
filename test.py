import os
import shutil


def clean_directory(directory_path):

    # Проходим по содержимому директории
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        try:
            # Удаляем файлы
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
                print(f"Файл {file_path} удален.")
            # Удаляем директории и их содержимое
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
                print(f"Директория {file_path} удалена.")
        except Exception as e:
            print(f"Ошибка при удалении {file_path}: {e}")


