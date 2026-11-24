# Issues del Organizador de Descargas

El líder del equipo crea estos issues en GitHub (**Issues → New issue**), copiando el título y la descripción, y le asigna cada uno a un integrante (**Assignees**). Las etiquetas (**Labels**) ya vienen en GitHub.

Van del más fácil al más difícil. Equipo de 2: issues 1 a 4 · equipo de 3: 1 a 6 · equipo de 4: 1 a 6, más uno que propongan ustedes.

---

## 1. `docs: mejorar el README`
**Label:** `documentation`

Completar el README para que alguien que no conoce el proyecto lo entienda: qué problema resuelve, cómo se usa, un ejemplo de lo que muestra en pantalla y quiénes lo hicieron.

**Listo cuando:**
- [ ] El README explica qué hace y cómo se usa
- [ ] Tiene un ejemplo de la salida
- [ ] Tiene los nombres del equipo

---

## 2. `feat: agregar la categoría Instaladores`
**Label:** `good first issue`

Los archivos `.exe` y `.msi` hoy van a *Otros*. Deben ir a una carpeta nueva llamada *Instaladores*.

**Listo cuando:**
- [ ] Los `.exe` y `.msi` van a *Instaladores*
- [ ] Lo probé con `crear_desorden.py`
- [ ] Actualicé el README con este cambio

---

## 3. `feat: mostrar cuántos archivos fueron a cada categoría`
**Label:** `enhancement`

Al terminar, además del total, mostrar el detalle. Por ejemplo:
```
Imagenes: 3 · Documentos: 4 · Videos: 2 · Otros: 2
```

**Listo cuando:**
- [ ] Muestra el conteo de cada categoría al final
- [ ] Los números coinciden con lo que hay en las carpetas
- [ ] Actualicé el README con este cambio

---

## 4. `feat: guardar un historial`
**Label:** `enhancement`

Cada vez que se ejecute, agregar al archivo `historial.txt` la fecha, la hora y la lista de archivos que movió. El historial no se borra: se va acumulando.

**Listo cuando:**
- [ ] Se crea `historial.txt` con la fecha y la hora
- [ ] Al ejecutarlo dos veces, el historial tiene las dos ejecuciones
- [ ] Actualicé el README con este cambio

---

## 5. `fix: no sobrescribir archivos con el mismo nombre`
**Label:** `bug`

**Este es un error real del script:** si en la carpeta de destino ya existe un archivo con el mismo nombre, el script se detiene con un error (en Windows) o reemplaza el archivo y se pierde (en Mac o Linux). Pruébalo: después de organizar, crea otro archivo llamado `meme.gif` directamente en `descargas_de_prueba` y vuelve a ejecutar `organizador.py`. Hay que renombrar el nuevo, por ejemplo `foto.jpg` → `foto (2).jpg`.

**Listo cuando:**
- [ ] Si el nombre ya existe, el archivo nuevo se renombra
- [ ] No se pierde ningún archivo
- [ ] Explico en el PR cómo lo probé
- [ ] Actualicé el README con este cambio

---

## 6. `feat: usarlo con mis Descargas de verdad`
**Label:** `enhancement`

Cambiar la carpeta por la carpeta de Descargas real del computador y, **antes de mover nada, preguntar**:
```
Voy a ordenar 245 archivos en C:\Users\...\Downloads. ¿Continuar? (s/n)
```
Si la respuesta no es `s`, no se mueve nada.

**Listo cuando:**
- [ ] Encuentra la carpeta de Descargas del usuario (pista: `Path.home() / "Downloads"`)
- [ ] Pregunta antes de mover y respeta la respuesta
- [ ] Lo probé primero con la carpeta de prueba
- [ ] Actualicé el README con este cambio

---

## 7. (Equipos de 4) Su propia mejora
**Label:** `enhancement`

Propongan una mejora o una forma de aplicar el organizador a algo real: su proyecto formativo, su trabajo, su celular. Escriban el issue ustedes mismos, con su lista de **Listo cuando**, que incluya actualizar el README.
