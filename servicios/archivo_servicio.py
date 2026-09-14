import json
import os

class ArchivoServicio:
    @staticmethod
    def cargar_json(nombre_archivo, datos_defecto=None):
        if datos_defecto is None:
            datos_defecto = []
            
        if not os.path.exists(nombre_archivo):
            ArchivoServicio.guardar_json(nombre_archivo, datos_defecto)
            return datos_defecto
            
        try:
            with open(nombre_archivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return datos_defecto

    @staticmethod
    def guardar_json(nombre_archivo, datos):
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)
