from pathlib import Path

import PIL.Image

import PIL.ExifTags

import shutil

import tkinter as tk



so_oft_keine_daten = 0

global liste_bilder
liste_bilder = []

liste_monate = ["platzhalter", "_Januar", "_Februar", "_März", "_April", "_Mai", "_Juni", "_Juli", "_August",
                "_September", "_Oktober", "_November", "_Dezember"]


foolproof = 0
foolproof_2 = 0
foolproof_3 = 0

window = tk.Tk()

window.title("Foto-Sortierer")

def center_window(window, width, height):

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)


    window.geometry('%dx%d+%d+%d' % (width, height, x, y))


center_window(window, 800, 800)









def main():
    eingabe_pfad_def()








def eingabe_pfad_def():
    global pfad_eingabe_text, Bestätigen_Quellpfad, pfad_eingabe_tk
    pfad_eingabe_text = tk.Label(text="""Bitte kopiere den Dateipfad, in dem sich die zu sortierenden Bilder befinden hinein!
    (Disclaimer: Bei falscher Angabe, könnte das Programm nicht funktionieren)""")
    pfad_eingabe_text.pack()

    pfad_eingabe_tk = tk.Entry(
        width=50,
    )
    pfad_eingabe_tk.pack()

    Bestätigen_Quellpfad = tk.Button(
        text="Bestätigen",
        command=get_eingabe_pfad,
        width=15
    )
    Bestätigen_Quellpfad.pack()


def get_eingabe_pfad():
    global eingabe_pfad, foolproof
    foolproof += 1
    eingabe_pfad = pfad_eingabe_tk.get()
    print(eingabe_pfad)

    if foolproof == 1:
        vorschau_liste_def()
        eingabe_pfadziel_def()

def vorschau_liste_def():
    path = Path(rf'{eingabe_pfad}')
    for path in path.iterdir():
        if path.suffix in ['.jpg', '.png', '.jpeg']:
            liste_bilder.append(path.name)#
    vorschau_liste = tk.Label(text=f"""
    
    
{liste_bilder[0], liste_bilder[1], liste_bilder[2]}""")
    vorschau_liste.pack()
    vorschau_info = tk.Label(text="""^^^ Hier ist eine Vorschau der Dateien, die sich in dem angegebenen Quellpfad befinden. Fahre fort, wenn es stimmt ^^^
""")
    vorschau_info.pack()












def eingabe_pfadziel_def():
    pfad_ziel_text = tk.Label(text="""

    Bitte kopiere den Dateipfad, in dem sich die Bilder nach der Sortierung befinden sollen, oder [1], wenn sie im
    gleichen Verzeichis sortiert werden sollen, wo sie sich jetzt befinden!
    (Disclaimer: Bei falscher Angabe, könnte das Programm nicht funktionieren)""")
    pfad_ziel_text.pack()

    global pfadziel_eingabe_tk
    pfadziel_eingabe_tk = tk.Entry(
        width=50,
    )
    pfadziel_eingabe_tk.pack()

    Bestätigen_Zielpfad = tk.Button(
        width=15,
        text="Bestätigen",
        command=get_eingabe_zielpfad
    )
    Bestätigen_Zielpfad.pack()


def get_eingabe_zielpfad():
    global eingabe_pfadziel, foolproof_2
    foolproof_2 += 1
    eingabe_pfadziel = pfadziel_eingabe_tk.get()
    if eingabe_pfadziel == "1":
        eingabe_pfadziel = eingabe_pfad
    print(eingabe_pfadziel)

    if foolproof_2 == 1:
        kopieren_verschieben()







def kopieren_verschieben():
    text_kov = tk.Label(text="""
    
    
    Willst du die Bilder in die Ordner kopieren oder verschieben ?""")
    text_kov.pack()

    frame = tk.Frame(window)
    frame.pack()
    global knopf_verschieben
    knopf_verschieben = tk.Button(frame,width=15, text="verschieben",command=verschieben_variable)
    knopf_verschieben.pack(side=tk.LEFT)
    global knopf_kopieren
    knopf_kopieren = tk.Button(frame,width=15, text="kopieren", command=kopieren_variable)
    knopf_kopieren.pack(side=tk.LEFT)

def verschieben_variable():
    global eingabe_kv, foolproof_3
    foolproof_3 += 1
    eingabe_kv = 2
    print(eingabe_kv)
    knopf_verschieben.config(bg="green")
    knopf_kopieren.config(bg="SystemButtonFace")
    if foolproof_3 == 1:
        eingabe_sortierung_def()
def kopieren_variable():
    global eingabe_kv, foolproof_3
    foolproof_3 += 1
    eingabe_kv = 1
    print(eingabe_kv)
    knopf_kopieren.config(bg="green")
    knopf_verschieben.config(bg="SystemButtonFace")
    if foolproof_3 == 1:
        eingabe_sortierung_def()



def eingabe_sortierung_def():
    text_sortierung = tk.Label(text="""
    
    
    Wie willst du die Bilder sortieren ?""")
    text_sortierung.pack()

    global knopf_sortieren_1, knopf_sortieren_2, knopf_sortieren_3, knopf_sortieren_4, knopf_sortieren_5, knopf_sortieren_6

    knopf_sortieren_1=tk.Button(
        text="Jahr",
        command=knopf_sortieren_def_1,
        width=15
    )
    knopf_sortieren_1.pack()



    knopf_sortieren_2 = tk.Button(
        text="Jahr > Monat",
        command=knopf_sortieren_def_2,
        width=15
    )
    knopf_sortieren_2.pack()



    knopf_sortieren_3 = tk.Button(
        text="Jahr > Monat > Tag",
        command=knopf_sortieren_def_3,
        width=15
    )
    knopf_sortieren_3.pack()



    knopf_sortieren_4 = tk.Button(
        text="Jahr > Tag",
        command=knopf_sortieren_def_4,
        width=15
    )
    knopf_sortieren_4.pack()



    knopf_sortieren_5 = tk.Button(
        text="Monat",
        command=knopf_sortieren_def_5,
        width=15
    )
    knopf_sortieren_5.pack()



    knopf_sortieren_6 = tk.Button(
        text="Monat > Tag",
        command=knopf_sortieren_def_6,
        width=15
    )
    knopf_sortieren_6.pack()

    leeres_label = tk.Label(text=f"""
    
    """)
    leeres_label.pack()

    knopf_sortieren_bestätigen = tk.Button(
        text="Bestätigen",
        command=sortieren_bestätigt,
        width=15
    )
    knopf_sortieren_bestätigen.pack()


def sortieren_bestätigt():
    sortierung()



def knopf_sortieren_def_1():
    global eingabe_sortierung
    eingabe_sortierung = 1
    knopf_sortieren_1.config(bg="green")
    knopf_sortieren_2.config(bg="SystemButtonFace")
    knopf_sortieren_3.config(bg="SystemButtonFace")
    knopf_sortieren_4.config(bg="SystemButtonFace")
    knopf_sortieren_5.config(bg="SystemButtonFace")
    knopf_sortieren_6.config(bg="SystemButtonFace")


def knopf_sortieren_def_2():

    global eingabe_sortierung
    eingabe_sortierung = 2
    knopf_sortieren_2.config(bg="green")
    knopf_sortieren_1.config(bg="SystemButtonFace")
    knopf_sortieren_3.config(bg="SystemButtonFace")
    knopf_sortieren_4.config(bg="SystemButtonFace")
    knopf_sortieren_5.config(bg="SystemButtonFace")
    knopf_sortieren_6.config(bg="SystemButtonFace")


def knopf_sortieren_def_3():

    global eingabe_sortierung
    eingabe_sortierung = 3
    knopf_sortieren_3.config(bg="green")
    knopf_sortieren_1.config(bg="SystemButtonFace")
    knopf_sortieren_2.config(bg="SystemButtonFace")
    knopf_sortieren_4.config(bg="SystemButtonFace")
    knopf_sortieren_5.config(bg="SystemButtonFace")
    knopf_sortieren_6.config(bg="SystemButtonFace")


def knopf_sortieren_def_4():

    global eingabe_sortierung
    eingabe_sortierung = 4
    knopf_sortieren_4.config(bg="green")
    knopf_sortieren_1.config(bg="SystemButtonFace")
    knopf_sortieren_2.config(bg="SystemButtonFace")
    knopf_sortieren_3.config(bg="SystemButtonFace")
    knopf_sortieren_5.config(bg="SystemButtonFace")
    knopf_sortieren_6.config(bg="SystemButtonFace")


def knopf_sortieren_def_5():

    global eingabe_sortierung
    eingabe_sortierung = 5
    knopf_sortieren_5.config(bg="green")
    knopf_sortieren_1.config(bg="SystemButtonFace")
    knopf_sortieren_2.config(bg="SystemButtonFace")
    knopf_sortieren_3.config(bg="SystemButtonFace")
    knopf_sortieren_4.config(bg="SystemButtonFace")
    knopf_sortieren_6.config(bg="SystemButtonFace")


def knopf_sortieren_def_6():

    global eingabe_sortierung
    eingabe_sortierung = 6
    knopf_sortieren_6.config(bg="green")
    knopf_sortieren_1.config(bg="SystemButtonFace")
    knopf_sortieren_2.config(bg="SystemButtonFace")
    knopf_sortieren_3.config(bg="SystemButtonFace")
    knopf_sortieren_4.config(bg="SystemButtonFace")
    knopf_sortieren_5.config(bg="SystemButtonFace")


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


def sortierung():
    global so_oft_keine_daten, ziel
    a = 0
    for m in liste_bilder:
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

        if eingabe_kv == 1:
            kopieren(quelle, ziel)
        elif eingabe_kv == 2:
            verschieben(quelle, ziel)
        a += 1


def end_screen():
    Bestätigen_Quellpfad.pack_forget()




    keine_daten_text = tk.Label(text=f"""
    
   
In {so_oft_keine_daten} Bildern wurde das DateTime Attribut nicht in den EXIF-Daten der Datei gefunden, sie wurden in den Ordner 'kein_datum' kopiert/verschoben.   
""")
    keine_daten_text.pack()


main()





window.mainloop()
