.. image:: https://img.shields.io/badge/license-LGPL--3-green.svg
    :target: https://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3

Notificación push desde ChatBox
===============================
# 📝 Traductor automático de archivos `.po` para módulos de Odoo (vía Google Translate)

Este script permite traducir automáticamente archivos `.po` de módulos de Odoo utilizando Google Translate mediante scraping ligero (sin necesidad de claves API). Es especialmente útil para módulos comunitarios que están solo en inglés y necesitan ser localizados rápidamente.

## 🚀 ¿Para qué sirve?

- Traducir al español (o cualquier otro idioma) los archivos `.po` de módulos de Odoo que vienen sin localización.
- Rellenar automáticamente los campos `msgstr` vacíos con la traducción correspondiente del `msgid`.
- Evitar la dependencia de APIs de pago como Google Cloud o DeepL.
- Ahorrar tiempo y esfuerzo en la localización de módulos, tanto para entornos de desarrollo como para producción.

## ⚙️ Características

- ✅ Traducción automática usando el endpoint web de Google Translate (no oficial).
- ✅ Solo traduce las entradas vacías (`msgstr == ""`), respetando las ya traducidas.
- ✅ Uso por línea de comandos, flexible y rápido.
- ✅ Compatible con cualquier sistema operativo que tenga Python (Windows, Linux, macOS).
- 🕓 Añade espera automática entre traducciones para evitar bloqueos de IP.
- 📦 Código limpio, portable, sin dependencias externas pesadas.

Configuración
==============
## 📦 Requisitos

- Python 3.7 o superior
- Librerías necesarias:

```bash
pip install polib requests

🖥️ Uso
=======
Ejecuta el script con los nombres del archivo de entrada y salida como argumentos:

```bash
python TRADUCTOR DE ARCHIVOS - PO.py archivo_entrada.po archivo_salida.po
🔁 Ejemplo:
===========
```bash
python TRADUCTOR DE ARCHIVOS - PO.py product.pot product_es.po
Esto leerá el archivo product.pot, traducirá todas las cadenas que no tengan traducción (msgstr vacío), y generará un nuevo archivo llamado product_es.po con las traducciones aplicadas.
📌 Consideraciones
===================
- ✅ Utiliza una interfaz web no oficial de Google Translate (translate.googleapis.com). Es funcional, pero no está garantizada ni diseñada para usos masivos o comerciales.

- 🕑 Para archivos muy extensos se recomienda incrementar el tiempo de espera entre peticiones (time.sleep) para evitar ser bloqueado temporalmente.

- ❌ No reemplaza soluciones profesionales para traducción masiva con control de calidad, pero es ideal para entornos rápidos, prototipos y módulos internos.

🛠️ Próximas mejoras
===================
* Selección de idioma origen y destino desde el propio script.
* Traducción de cadenas msgid_plural y msgstr[n].
* Interfaz gráfica básica para usuarios no técnicos.
* Soporte para múltiples archivos y carpetas en batch.

Compañía
-------
* `Infinity Draw <https://infinitydraw.es/>`__

Licencia
-------
Lesser General Public License, Version 3 (LGPL v3).
(https://www.gnu.org/licenses/lgpl-3.0-standalone.html)

Créditos
-------
Desarrollador: (V17) Fernan Nerd , Contacto: contacto@infinitydraw.es

Contactos
--------
* E-Mail de Contacto : contacto@infinitydraw.es
* Sitio Web : https://infinitydraw.es

Localizador de errores o bugs
-----------
De momento no hay seguimiento de rastreo de errores.

Mantenedor
==========
.. image:: https://cloud.infinitydraw.es/files/index.php/s/Rc9xpN3k6mGbtjD/download
   :target: https://infinitydraw.es

Este script es mantenido por Infinity Draw.

Preguntas e información, en `En nuestro sitio Web <https://infinitydraw.es/>`__

Más información
===================
HTML Descripción: `<static/description/index.html>`__