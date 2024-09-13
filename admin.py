import json
import os


def add_to_json(file_path, new_data):
    """
    Добавляет новое значение в JSON файл.

    :param file_path: Путь к JSON файлу.
    :param new_data: Новый словарь для добавления в JSON файл.
    """
    try:
        # Проверка существования файла
        if not os.path.exists(file_path):
            print(f"Файл {file_path} не найден. Создаем новый файл.")
            data = {}
        else:
            # Открываем файл и загружаем данные
            with open(file_path, "r", encoding="utf-8") as json_file:
                try:
                    data = json.load(json_file)
                    print(f"Данные из файла {file_path} загружены.")
                except json.JSONDecodeError:
                    print(f"Файл {file_path} пустой или поврежден. Создаем пустую структуру.")
                    data = {}

        # Обновляем данные новыми значениями
        data.update(new_data)

        # Сохраняем обновлённые данные в файл
        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
            print(f"Данные успешно обновлены в файле {file_path}.")

    except Exception as e:
        print(f"Произошла ошибка: {e}")