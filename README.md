# Organizador de Descargas

## ¿Qué problema resuelve?

Con el uso diario, la carpeta de Descargas se llena de fotos, documentos PDF, videos, canciones y archivos comprimidos mezclados en un mismo lugar, haciendo que encontrar cualquier archivo tome varios minutos.

Este script en Python revisa una carpeta desordenada y clasifica automáticamente cada archivo en una subcarpeta según su extensión: **Imagenes**, **Documentos**, **Videos**, **Musica**, **Comprimidos** y **Otros**.

## Cómo usarlo

Solo necesitas Python 3 instalado. No hay que instalar nada, ni crear un entorno virtual.

1. Clona este repositorio y entra a la carpeta del proyecto:
   ```bash
   git clone https://github.com/itztsukuyomi/organizador-descargas.git
   cd organizador-descargas
   ```

2. Genera la carpeta de prueba y ejecuta el organizador:
   ```bash
   python crear_desorden.py      # crea una carpeta de prueba revuelta
   python organizador.py         # la ordena
   ```

Si `python` no funciona en tu computador, usa `py`.

`crear_desorden.py` se puede ejecutar las veces que quieras: siempre deja la carpeta revuelta otra vez. Así pruebas sin riesgo, sin tocar tus archivos reales.

## Ejemplo de salida

Al ejecutar `python organizador.py`, la consola muestra los archivos clasificados y el resumen del proceso:

```text
Organizando descargas_de_prueba...
  foto_1.jpg -> Imagenes
  documento_1.pdf -> Documentos
  video_1.mp4 -> Videos
  cancion_1.mp3 -> Musica
  comprimido_1.zip -> Comprimidos
  archivo_1.txt -> Otros
Organicé 56 archivos en 0.01 segundos
```

## Lo que vas a aprender con este script

| Concepto | Dónde está en el código | Qué hace |
|---|---|---|
| **Variable** | `CARPETA = Path("descargas_de_prueba")` | Guarda un dato para usarlo después |
| **Diccionario** | `CATEGORIAS = { "Imagenes": [...], ... }` | Relaciona cada categoría con su lista de extensiones |
| **Lista** | `[".jpg", ".jpeg", ".png"]` | Guarda varios valores en orden |
| **Función** | `def categoria_de(archivo):` | Un bloque de código con nombre, que se puede usar muchas veces |
| **Ciclo `for`** | `for archivo in carpeta.iterdir():` | Repite lo mismo con cada archivo de la carpeta |
| **Condicional `if`** | `if extension in extensiones:` | Decide qué hacer según una condición |
| **Contador** | `movidos += 1` | Suma uno cada vez que mueve un archivo |
| **Módulos** | `import shutil`, `import time` | Herramientas que ya trae Python: mover archivos y medir el tiempo |
| **f-string** | `f"Organicé {movidos} archivos"` | Arma un texto con valores adentro |

## Cómo está organizado el código

1. **Configuración** (arriba): la carpeta a ordenar y las categorías. Casi todos los cambios empiezan aquí.
2. **`categoria_de()`**: mira la extensión de un archivo y decide su categoría.
3. **`organizar()`**: recorre la carpeta, mueve cada archivo y cuenta cuántos movió y cuánto se demoró.
4. **`if __name__ == "__main__":`**: lo que se ejecuta cuando corres `python organizador.py`.

## Equipo

* Juan Manuel Saldarriaga (Líder)
* Jose
* Sebas
* Papelito