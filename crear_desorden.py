"""
Crea la carpeta 'descargas_de_prueba' con 56 archivos de ejemplo revueltos,
para probar el organizador sin tocar tus archivos reales.
Puedes ejecutarlo las veces que quieras: siempre deja la carpeta revuelta.
"""

from pathlib import Path
import shutil

CARPETA = Path("descargas_de_prueba")

# Nombres como los que aparecen en una carpeta de Descargas real
ARCHIVOS = [
    # Imágenes
    "IMG_20261103_2041.jpg", "WhatsApp Image 2026-11-10.jpeg", "captura_clase_git.png",
    "meme_gato_programador.gif", "foto_perfil_linkedin.webp", "fondo_pantalla.jpg",
    "foto_carnet_sena.png", "screenshot_error.png", "logo_proyecto.png", "atardecer.jpg",
    # Documentos
    "hoja_de_vida_2026.pdf", "certificado_sena.pdf", "notas_clase.txt", "presupuesto_mes.xlsx",
    "taller_git_ramas.docx", "exposicion_proyecto.pptx", "lista_mercado.txt",
    "factura_epm_noviembre.pdf", "horario_trimestre.xlsx", "requisitos_proyecto.docx",
    "base_de_datos_clientes.csv", "guia_portafolio.pdf",
    # Videos
    "video_tiktok_baile.mp4", "clase_grabada_martes.mov", "tutorial_python.mp4",
    "partido_futbol_final.mkv", "presentacion_equipo.avi", "historia_instagram.mp4",
    # Música y audio
    "cancion_favorita.mp3", "nota_de_voz_mama.m4a", "podcast_tecnologia.mp3",
    "ringtone_nuevo.mp3", "grabacion_reunion.wav",
    # Comprimidos
    "proyecto_final_v2.zip", "fotos_paseo.zip", "plantilla_portafolio.zip",
    "drivers_impresora.rar", "respaldo_tareas.7z",
    # Otros (sin categoría todavía)
    "instalador_juego.exe", "setup_vscode.exe", "python_installer.exe",
    "archivo_raro.xyz", "configuracion.ini", "acceso_directo.lnk",
    "programa_contable.msi", "documento_sin_extension", "mapa_metro.kml",
    "contrasenas_NO_ABRIR.txt", "factura_celular.pdf", "musica_gimnasio.mp3",
    "IMG_20261115_0932.jpg", "WhatsApp Video 2026-11-12.mp4", "trabajo_grupal_final.docx",
    "certificado_curso_ingles.pdf", "Captura de pantalla 2026-11-18.png", "evidencia_RA1.zip",
]

if CARPETA.exists():
    shutil.rmtree(CARPETA)              # Empieza siempre desde cero
CARPETA.mkdir()

for nombre in ARCHIVOS:
    (CARPETA / nombre).write_text(f"Archivo de prueba: {nombre}", encoding="utf-8")

print(f"Listo: '{CARPETA}' tiene {len(ARCHIVOS)} archivos revueltos.")
print("Ahora ejecuta:  python organizador.py")
