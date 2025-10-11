import json
import os

INVENTARIO_FILE = "inventario.json"
inventario = {}


def cargar_inventario():
    global inventario
    if os.path.exists(INVENTARIO_FILE):
        with open(INVENTARIO_FILE, "r", encoding="utf-8") as f:
            inventario = json.load(f)
    else:
        inventario = {}


def guardar_inventario():
    with open(INVENTARIO_FILE, "w", encoding="utf-8") as f:
        json.dump(inventario, f, ensure_ascii=False, indent=2)
