from pathlib import Path

import PIL.Image

import PIL.ExifTags

liste_bilder = []

path = Path(r'C:\Users\intern1\Documents\Fotos-sortieren\Ablage-Bilder')
for path in path.iterdir():
    if path.suffix in ['.jpg', '.png', '.jpeg']:
        liste_bilder.append(path.name)

img = PIL.Image.open(r'C:\Users\intern1\Documents\Fotos-sortieren\Ablage-Bilder\51370198468_f3fde7f405_o.jpg')
exif_data = img.getexif()

exif = {
    PIL.ExifTags.TAGS[k]: v
    for k, v in img.getexif().items()
    if k in PIL.ExifTags.TAGS
}

datumuhrzeit = exif['DateTime']












print(liste_bilder)


print(exif)

if 'DateTime' in exif:
    print(datumuhrzeit)
else:
    print("DateTime attribute not found in the image's EXIF data.")

jahr = ""
i = 0
while i < 4:
    jahr = jahr + datumuhrzeit[i]
    i = i + 1

print(jahr)

monat = ""
o = 5
while o < 7:
    monat = monat + datumuhrzeit[o]
    o = o + 1

print(monat)

p = Path(rf'C:\Users\intern1\Documents\Fotos-sortieren\Ablage-Bilder\{jahr}')
p.mkdir(parents=True, exist_ok=True)

