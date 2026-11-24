"""
ORGANIZADOR DE DESCARGAS
========================
Toma una carpeta desordenada y mueve cada archivo a una subcarpeta
según su tipo: Imagenes, Documentos, Videos, Musica, Comprimidos, Otros.

Cómo usarlo:
    1. Crea la carpeta de prueba:   python crear_desorden.py
    2. Ordénala:                    python organizador.py

Solo usa módulos que ya vienen con Python. No hay que instalar nada.
"""

from pathlib import Path   # Para trabajar con carpetas y archivos
import shutil              # Para mover archivos
import time                # Para medir cuánto se demora

# ------------------------------------------------------------------
# CONFIGURACIÓN: cambia estos valores para adaptar el organizador
# ------------------------------------------------------------------

# Carpeta que se va a ordenar. Empezamos con una de prueba para no
# tocar tu carpeta de Descargas real.
CARPETA = Path("descargas_de_prueba")

# Cada categoría y las extensiones que le pertenecen
CATEGORIAS = {
    "Imagenes":    [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documentos":  [".pdf", ".docx", ".xlsx", ".pptx", ".txt", ".csv"],
    "Videos":      [".mp4", ".mov", ".avi", ".mkv"],
    "Musica":      [".mp3", ".wav", ".m4a"],
    "Comprimidos": [".zip", ".rar", ".7z"],
}


def categoria_de(archivo):
    """Devuelve el nombre de la categoría según la extensión del archivo."""
    extension = archivo.suffix.lower()          # ".PDF" -> ".pdf"
    for categoria, extensiones in CATEGORIAS.items():
        if extension in extensiones:
            return categoria
    return "Otros"                              # Si no está en ninguna


def organizar(carpeta):
    """Mueve cada archivo de la carpeta a la subcarpeta de su categoría."""
    if not carpeta.exists():
        print(f"No encontré la carpeta '{carpeta}'. ¿Ejecutaste crear_desorden.py?")
        return

    inicio = time.time()                        # Empieza el cronómetro
    movidos = 0                                 # Contador de archivos movidos

    for archivo in carpeta.iterdir():           # Recorre lo que hay adentro
        if archivo.is_file():                   # Ignora las carpetas
            categoria = categoria_de(archivo)
            destino = carpeta / categoria
            destino.mkdir(exist_ok=True)        # Crea la subcarpeta si no existe
            shutil.move(str(archivo), str(destino / archivo.name))
            print(f"  {archivo.name}  ->  {categoria}/")
            movidos += 1                        # Suma uno al contador

    segundos = time.time() - inicio             # Detiene el cronómetro
    print(f"\n¡Listo! Organicé {movidos} archivos en {segundos:.3f} segundos.")


# Esto se ejecuta cuando corres:  python organizador.py
if __name__ == "__main__":
    print(f"Organizando '{CARPETA}'...\n")
    organizar(CARPETA)
