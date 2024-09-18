import requests

def upload_image_to_fileio(image_path):
    url = 'https://file.io'


    with open(image_path, 'rb') as image_file:
        files = {'file': image_file}
        response = requests.post(url, files=files)
    image_file.close()

    # Проверяем успешность загрузки
    if response.status_code == 200:
        file_url = response.json().get('link')
        print("Изображение загружено! URL:", file_url)
        return file_url
    else:
        print("Ошибка загрузки:", response.status_code, response.text)
        return None


