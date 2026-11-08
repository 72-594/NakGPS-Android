"""Prepara el proyecto Android generado por Capacitor: permisos de ubicación, nombre e ícono."""
import os, re
from PIL import Image, ImageDraw

RES = "android/app/src/main/res"
MANIFEST = "android/app/src/main/AndroidManifest.xml"

# 1) Permisos de ubicación (necesarios para el punto azul)
m = open(MANIFEST, encoding="utf-8").read()
if "ACCESS_FINE_LOCATION" not in m:
    perms = ('\n    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />'
             '\n    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />')
    m = re.sub(r'(<uses-permission android:name="android.permission.INTERNET"\s*/>)', r'\1' + perms, m, count=1)
    assert "ACCESS_FINE_LOCATION" in m, "No se encontró el permiso INTERNET en el manifiesto"
    open(MANIFEST, "w", encoding="utf-8").write(m)

# 2) Ícono: brújula blanca sobre verde
GREEN = (14, 138, 106, 255)

def draw(size, adaptive):
    S = size * 4
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if not adaptive:  # ícono clásico con fondo redondeado
        d.rounded_rectangle([0, 0, S, S], radius=int(S * 0.22), fill=GREEN)
    c = S / 2
    k = S * (0.30 if adaptive else 0.36)   # radio del aro (zona segura en adaptativo)
    d.ellipse([c - k, c - k, c + k, c + k], outline=(255, 255, 255, 255), width=max(2, int(S * 0.035)))
    n = k * 0.78
    d.polygon([(c, c - n), (c + n * 0.34, c + n * 0.12), (c - n * 0.34, c + n * 0.12)], fill=(255, 255, 255, 255))
    d.polygon([(c, c + n), (c + n * 0.34, c - n * 0.12), (c - n * 0.34, c - n * 0.12)], fill=(240, 122, 38, 255))
    d.ellipse([c - S * 0.03, c - S * 0.03, c + S * 0.03, c + S * 0.03], fill=GREEN)
    return img.resize((size, size), Image.LANCZOS)

legacy = {"mdpi": 48, "hdpi": 72, "xhdpi": 96, "xxhdpi": 144, "xxxhdpi": 192}
fore = {"mdpi": 108, "hdpi": 162, "xhdpi": 216, "xxhdpi": 324, "xxxhdpi": 432}
for dens, px in legacy.items():
    folder = f"{RES}/mipmap-{dens}"
    os.makedirs(folder, exist_ok=True)
    draw(px, False).save(f"{folder}/ic_launcher.png")
    draw(px, False).save(f"{folder}/ic_launcher_round.png")
    draw(fore[dens], True).save(f"{folder}/ic_launcher_foreground.png")

bg = f"{RES}/values/ic_launcher_background.xml"
os.makedirs(os.path.dirname(bg), exist_ok=True)
open(bg, "w", encoding="utf-8").write(
    '<?xml version="1.0" encoding="utf-8"?>\n<resources>\n    <color name="ic_launcher_background">#0E8A6A</color>\n</resources>\n')
print("Android preparado: permisos de ubicación e ícono listos.")
