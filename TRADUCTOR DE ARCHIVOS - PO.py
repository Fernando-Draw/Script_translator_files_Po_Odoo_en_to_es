import polib
import requests
import time
import urllib.parse
import sys

HEADERS = {
    "User-Agent": "Mozilla/5.0",
}

def traducir_google(texto, source="en", target="es"):
    if not texto.strip():
        return ''
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={source}&tl={target}&dt=t&q={urllib.parse.quote(texto)}"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        traduccion = response.json()[0][0][0]
        return traduccion
    except Exception as e:
        print(f"[ERROR] Traducción fallida: {texto} → {e}")
        return ""

def traducir_archivo_po(archivo_entrada, archivo_salida):
    po = polib.pofile(archivo_entrada)
    for entrada in po:
        if not entrada.msgstr.strip() and entrada.msgid.strip():
            print(f"[...] Traduciendo: {entrada.msgid}")
            traduccion = traducir_google(entrada.msgid)
            entrada.msgstr = traduccion
            print(f"[OK] {entrada.msgid} → {traduccion}")
            time.sleep(1.5)  # Pausa ligera entre traducciones
    po.save(archivo_salida)
    print(f"\n✅ Archivo traducido guardado en: {archivo_salida}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python traducir_po.py <archivo_entrada.po> <archivo_salida.po>")
    else:
        archivo_entrada = sys.argv[1]
        archivo_salida = sys.argv[2]
        traducir_archivo_po(archivo_entrada, archivo_salida)