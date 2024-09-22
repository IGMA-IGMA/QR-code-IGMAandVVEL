import re

def validate_rgb(rgb):
    rgb = rgb.strip().split(",")
    if len(rgb) != 3:
        return False
    try:
        return all(0 <= int(value) <= 255 for value in rgb)
    except ValueError:
        return False

def validate_hex(hex_color):
    print(hex_color)
    return bool(re.fullmatch(r"^#[0-9A-Fa-f]{6}$", hex_color))
