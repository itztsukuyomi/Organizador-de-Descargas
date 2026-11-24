# Organizador de Descargas

Toma una carpeta desordenada y mueve cada archivo a una subcarpeta según su tipo: Imagenes, Documentos, Videos, Musica, Comprimidos y Otros.

> Este README es el punto de partida. Mejorarlo es uno de los issues del equipo.

## Cómo usarlo

Solo necesitas Python. No hay que instalar nada, ni crear un entorno virtual.

```
python crear_desorden.py      # crea una carpeta de prueba revuelta
python organizador.py         # la ordena
```

Si `python` no funciona en tu computador, usa `py`.

`crear_desorden.py` se puede ejecutar las veces que quieras: siempre deja la carpeta revuelta otra vez. Así pruebas sin riesgo, sin tocar tus archivos reales.

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
