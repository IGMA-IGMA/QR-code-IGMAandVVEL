import json


def update_setting_user(chat_id, color, width, height):
    with open("id_user.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    new_values = [color, width, height]

    data[chat_id][1] = new_values

    print(json.dumps(data, indent=4))

    with open("id_user.json", "w") as file:
        json.dump(data, file, indent=4)
    print("Значение обновленно")

