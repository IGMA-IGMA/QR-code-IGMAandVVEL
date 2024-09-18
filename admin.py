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
                data = json.load(json_file)
                print(f"Данные из файла {file_path} загружены.")

        # Обновляем данные новыми значениями
        data.update(new_data)

        # Сохраняем обновлённые данные в файл
        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
            print(f"Данные успешно обновлены в файле {file_path}.")
        json_file.close()

    except Exception as e:
        print(f"Произошла ошибка: {e}")


def user_is_admin(chat_id: str) -> bool:
    with open("db_user_tg/id_admin.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    json_file.close()
    return chat_id in data


def user_in_dbUser(chat_id: str) -> bool:
    with open("db_user_tg/id_user.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    json_file.close()
    return chat_id in data


def spisok_admin():
    with open("db_user_tg/id_admin.json", "r", encoding="utf-8") as json_file:
        file = json.load(json_file)
    data = []
    for i, (user_id, username) in enumerate(file.items(), 0):
        data.append(f"{i}. {user_id}: {username}")
    data = "\n".join(data)
    return data


def update_setting_user(chat_id, color, width, height):
    with open("db_user_tg/id_user.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    new_values = [color, width, height]

    data[chat_id][1] = new_values

    print(json.dumps(data, indent=4))

    with open("db_user_tg/id_user.json", "w") as file:
        json.dump(data, file, indent=4)
    print("Значение обновленно")
