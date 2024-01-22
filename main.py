from pathlib import Path

import PIL.Image

import PIL.ExifTags

import shutil

liste_bilder = []

liste_monate = ["platzhalter", "_Januar", "_Februar", "_März", "_April", "_Mai", "_Juni", "_Juli", "_August", "_September", "_Oktober", "_November", "_Dezember"]

path = Path(r'C:\Users\intern1\Pictures\sortierte-bilder')
for path in path.iterdir():
    if path.suffix in ['.jpg', '.png', '.jpeg']:
        liste_bilder.append(path.name)

print(liste_bilder)

while True:
    try:
        eingabe = int(input("""Willst du die Bilder in die Ordner kopieren[1] oder verschieben[2] ?
> """))
        break
    except ValueError:
        print("Biite gib 1 oder 2 ein!")


def kopieren(quellpfad, zielpfad):
    source = quellpfad

    destination = zielpfad

    shutil.copy(source, destination)


def verschieben(quellpfad, zielpfad):
    source = quellpfad

    destination = zielpfad

    shutil.move(source, destination)


def jahr_monat_ausgabe(bild, eingabe):
    img = PIL.Image.open(rf'C:\Users\intern1\Pictures\sortierte-bilder\{bild}')


    exif = {
        PIL.ExifTags.TAGS[k]: v
        for k, v in img.getexif().items()
        if k in PIL.ExifTags.TAGS
    }


    datumuhrzeit = ""

    quelle = rf'C:\Users\intern1\Pictures\sortierte-bilder\{bild}'

    if 'DateTime' in exif:
        datumuhrzeit = exif['DateTime']

        global jahr
        jahr = ""
        i = 0
        while i < 4:
            jahr = jahr + datumuhrzeit[i]
            i = i + 1
        p = Path(rf'C:\Users\intern1\Pictures\sortierte-bilder\{jahr}')
        p.mkdir(parents=True, exist_ok=True)

        monat = ""
        o = 5
        while o < 7:
            monat = monat + datumuhrzeit[o]
            o = o + 1

        monat = monat + liste_monate[int(monat)]
        p = Path(rf'C:\Users\intern1\Pictures\sortierte-bilder\{jahr}\{monat}')
        p.mkdir(parents=True, exist_ok=True)


        ziel = rf'C:\Users\intern1\Pictures\sortierte-bilder\{jahr}\{monat}'

        img.close()


        if eingabe == 1:
            kopieren(quelle, ziel)

        elif eingabe == 2:
            verschieben(quelle, ziel)

    else:
        print(f"DateTime Attribut nicht gefunden in den EXIF-Daten der Datei {bild} ,es wurde in den Ordner 'keindatum' kopiert/verschoben.")
        datumuhrzeit = 0000
        p = Path(rf'C:\Users\intern1\Pictures\sortierte-bilder\keindatum')
        p.mkdir(parents=True, exist_ok=True)

        ziel = rf'C:\Users\intern1\Pictures\sortierte-bilder\keindatum'

        img.close()

        if eingabe == 1:
            kopieren(quelle, ziel)

        elif eingabe == 2:
            verschieben(quelle, ziel)


a = 0
for i in liste_bilder:
    jahr_monat_ausgabe(liste_bilder[a], eingabe)
    a += 1

