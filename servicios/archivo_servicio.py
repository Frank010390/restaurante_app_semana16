import json
import os

class ArchivoServicio:
    def __init__(self):
        pass

    def cargar_json(self, ruta_archivo):
        if not os.path.exists(ruta_archivo):
            return []
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def guardar_json(self, ruta_archivo, datos):
        os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)
        with open(ruta_archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)