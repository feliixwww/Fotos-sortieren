from pathlib import Path

import PIL.Image

import PIL.ExifTags

import shutil



so_oft_keine_daten = 0

liste_bilder = []

liste_monate = ["platzhalter", "_Januar", "_Februar", "_März", "_April", "_Mai", "_Juni", "_Juli", "_August",
                "_September", "_Oktober", "_November", "_Dezember"]


eingabe_pfad = input("""
Bitte kopiere den Dateipfad, in dem sich die zu sortierenden Bilder befinden hinein!
(Disclaimer: Bei falscher Angabe, könnte das Programm nicht funktionieren)
> """)


eingabe_pfadziel = input("""
Bitte kopiere den Dateipfad, in dem sich die Bilder nach der Sortierung befinden sollen, oder [1], wenn sie im gleichen
Verzeichis sortiert werden sollen, wo sie sich jetzt befinden!
(Disclaimer: Bei falscher Angabe, könnte das Programm nicht funktionieren)
> """)

if eingabe_pfadziel == "1":
    eingabe_pfadziel = eingabe_pfad


path = Path(rf'{eingabe_pfad}')
for path in path.iterdir():
    if path.suffix in ['.jpg', '.png', '.jpeg']:
        liste_bilder.append(path.name)

print(f"""
{liste_bilder}""")

while True:
    try:
        eingabe = int(input("""^^^^^^^^^^ Hier ist eine Vorschau der Dateien, die sich in dem angegebenen Quellpfad befinden. Fahre fort, wenn es stimmt ^^^^^^^^^^
                 
Willst du die Bilder in die Ordner kopieren[1] oder verschieben[2] ?
> """))
        if eingabe in [1, 2]:
            break
        else:
            print("Biite gib 1 oder 2 ein!")
    except ValueError:
        print("Biite gib 1 oder 2 ein!")

while True:
    try:
        eingabe_sortierung = int(input("""
Wie willst du die Bilder sortieren ?

[1] Jahr
[2] Jahr > Monat
[3] Jahr > Monat > Tag
[4] Jahr > Tag
[5] Monat
[6] Monat > Tag

> """))
        if eingabe_sortierung in [1, 2, 3, 4, 5, 6]:
            break
        else:
            print("Biite gib eine der Zahlen ein!")
    except ValueError:
        print("Biite gib eine der Zahlen ein!")


def kopieren(source, destination):

    shutil.copy(source, destination)


def verschieben(source, destination):

    shutil.move(source, destination)


def exif_lesen(bild):
    img = PIL.Image.open(rf'{eingabe_pfad}\{bild}')

    exif = {
        PIL.ExifTags.TAGS[k]: v
        for k, v in img.getexif().items()
        if k in PIL.ExifTags.TAGS
    }


    datumuhrzeit = ""
    jahr = ""
    monat = ""
    tag = ""
    if 'DateTime' in exif:
        datumuhrzeit = exif['DateTime']
        i = 0
        while i < 4:
            jahr = jahr + datumuhrzeit[i]
            i = i + 1

        o = 5
        while o < 7:
            monat = monat + datumuhrzeit[o]
            o = o + 1
        monat = monat + liste_monate[int(monat)]

        p = 8
        while p < 10:
            tag = tag + datumuhrzeit[p]
            p = p + 1

    img.close()

    return jahr, monat, tag


a = 0
for i in liste_bilder:
    datum = exif_lesen(liste_bilder[a])
    quelle = rf'{eingabe_pfad}\{liste_bilder[a]}'
    if datum[0] != "":
        if eingabe_sortierung == 1:
            p = Path(rf'{eingabe_pfadziel}\{datum[0]}')
            p.mkdir(parents=True, exist_ok=True)
            ziel = rf'{eingabe_pfadziel}\{datum[0]}'

        elif eingabe_sortierung == 2:
            p = Path(rf'{eingabe_pfadziel}\{datum[0]}')
            p.mkdir(parents=True, exist_ok=True)
            p = Path(rf'{eingabe_pfadziel}\{datum[0]}\{datum[1]}')
            p.mkdir(parents=True, exist_ok=True)
            ziel = rf'{eingabe_pfadziel}\{datum[0]}\{datum[1]}'

        elif eingabe_sortierung == 3:
            p = Path(rf'{eingabe_pfadziel}\{datum[0]}')
            p.mkdir(parents=True, exist_ok=True)
            p = Path(rf'{eingabe_pfadziel}\{datum[0]}\{datum[1]}')
            p.mkdir(parents=True, exist_ok=True)
            p = Path(rf'{eingabe_pfadziel}\{datum[0]}\{datum[1]}\{datum[2]}')
            p.mkdir(parents=True, exist_ok=True)
            ziel = rf'{eingabe_pfadziel}\{datum[0]}\{datum[1]}\{datum[2]}'

        elif eingabe_sortierung == 4:
            p = Path(rf'{eingabe_pfadziel}\{datum[0]}')
            p.mkdir(parents=True, exist_ok=True)
            p = Path(rf'{eingabe_pfadziel}\{datum[0]}\{datum[1]} der_{datum[2]}te')
            p.mkdir(parents=True, exist_ok=True)
            ziel = rf'{eingabe_pfadziel}\{datum[0]}\{datum[1]} der_{datum[2]}te'

        elif eingabe_sortierung == 5:
            p = Path(rf'{eingabe_pfadziel}\{datum[1]}')
            p.mkdir(parents=True, exist_ok=True)
            ziel = rf'{eingabe_pfadziel}\{datum[1]}'

        elif eingabe_sortierung == 6:
            p = Path(rf'{eingabe_pfadziel}\{datum[1]}')
            p.mkdir(parents=True, exist_ok=True)
            p = Path(rf'{eingabe_pfadziel}\{datum[1]}\{datum[2]}')
            p.mkdir(parents=True, exist_ok=True)
            ziel = rf'{eingabe_pfadziel}\{datum[1]}\{datum[2]}'

    else:
        p = Path(rf'{eingabe_pfadziel}\kein_datum')
        p.mkdir(parents=True, exist_ok=True)
        ziel = rf'{eingabe_pfadziel}\kein_datum'
        so_oft_keine_daten = so_oft_keine_daten + 1

    if eingabe == 1:
        kopieren(quelle, ziel)
    elif eingabe == 2:
        verschieben(quelle, ziel)
    a += 1


print(f"""
In {so_oft_keine_daten} Bildern wurde das DateTime Attribut nicht in den EXIF-Daten der Datei gefunden, sie wurden in den Ordner 'kein_datum' kopiert/verschoben.""")


