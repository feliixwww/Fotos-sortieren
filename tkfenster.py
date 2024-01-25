from pathlib import Path

import PIL.Image

from PIL import ImageTk, Image

import PIL.ExifTags

import shutil

import tkinter as tk

liste_monate = ["platzhalter", "_Januar", "_Februar", "_März", "_April", "_Mai", "_Juni", "_Juli", "_August",
                "_September", "_Oktober", "_November", "_Dezember"]

window = tk.Tk()

window.title("Foto-Sortierer")


def center_window(window, width, height):

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    window.geometry('%dx%d+%d+%d' % (width, height, x, y))


leere_liste = []


idiot = 1

ort_im_code = 0


def main():
    center_window(window, 800, 825)
    global liste_bilder, so_oft_keine_daten, foolproof, foolproof_2, foolproof_3

    so_oft_keine_daten = 0

    liste_bilder = []

    foolproof = 0
    foolproof_2 = 0
    foolproof_3 = 0

    eingabe_pfad_def()


def eingabe_pfad_def():
    global pfad_eingabe_text, Bestätigen_Quellpfad, pfad_eingabe_tk, leeres_label_2, pfad_eingabe_als_label
    pfad_eingabe_text = tk.Label(text="""Bitte kopiere den Dateipfad, in dem sich die zu sortierenden Bilder befinden hinein!
    (Disclaimer: Bei falscher Angabe, könnte das Programm nicht funktionieren)""")
    pfad_eingabe_text.pack()

    pfad_eingabe_tk = tk.Entry(
        width=50,
    )
    pfad_eingabe_tk.pack()

    pfad_eingabe_als_label = tk.Label(
        text=""
    )
    pfad_eingabe_als_label.pack()

    Bestätigen_Quellpfad = tk.Button(
        text="Bestätigen",
        command=get_eingabe_pfad,
        width=15
    )
    Bestätigen_Quellpfad.pack()

    leeres_label_2 = tk.Label(text="\n")
    leeres_label_2.pack()

    if idiot == 2:
        leeres_label_2.config(fg="red", text=f"\nBitte gib ein gültiges Verzeichnis an, in dem sich Bilder befinden!\n")



def get_eingabe_pfad():
    global eingabe_pfad, foolproof, liste_bilder
    foolproof += 1

    eingabe_pfad = pfad_eingabe_tk.get()
    print(eingabe_pfad)

    liste_bilder = []

    if idiot == 2:
        leeres_label_2.pack_forget()
    eingabe_pfad_bestätigt()
    vorschau_liste_def()


def eingabe_pfad_bestätigt():
    Bestätigen_Quellpfad.pack_forget()
    pfad_eingabe_tk.pack_forget()

    pfad_eingabe_als_label.config(fg="green", text=f"\n\nAusgewählter Pfad:{eingabe_pfad}\n\n")
    pfad_eingabe_als_label.pack()


def eingabe_pfad_forget_def():
    Bestätigen_Quellpfad.pack_forget()
    pfad_eingabe_text.pack_forget()
    pfad_eingabe_tk.pack_forget()
    pfad_eingabe_als_label.pack_forget()


def vorschau_liste_def():
    global vorschau_liste, idiot, leeres_label_2

    path = Path(rf'{eingabe_pfad}')
    while True:
        try:
            for path in path.iterdir():
                if path.suffix in ['.jpg', '.png', '.jpeg']:
                    liste_bilder.append(path.name)
            return vorschau_bilder_def()
        except OSError:
            idiot = 2

            return eingabe_pfad_forget_def(), main()


def all_children(window):
    _list = window.winfo_children()

    for item in _list:
        if item.winfo_children():
            _list.extend(item.winfo_children())

    return _list


def neu_starten_def():
    widget_list = all_children(window)
    for item in widget_list:
        item.pack_forget()


def neu_starten_knopf_def():
    global idiot
    idiot = 1
    return neu_starten_def(), main()




def vorschau_bilder_def():
    global img_1_label, img_2_label, img_3_label, frame_3, vorschau_info, neu_starten_knopf_vorschau

    if not liste_bilder:
        idiot = 2
        print(idiot)
        return eingabe_pfad_forget_def(), main()

    frame_3 = tk.Frame(window)
    frame_3.pack()

    img_1 = Image.open(f"{eingabe_pfad}\{liste_bilder[0]}")
    img_1_klein = img_1.resize((100, 100))
    img_1_klein_fertig = ImageTk.PhotoImage(img_1_klein)
    img_1_label = tk.Label(frame_3)
    img_1_label.image = img_1_klein_fertig
    img_1_label['image'] = img_1_label.image
    img_1_label.pack(side=tk.LEFT)

    img_2 = Image.open(f"{eingabe_pfad}\{liste_bilder[1]}")
    img_2_klein = img_2.resize((100, 100))
    img_2_klein_fertig = ImageTk.PhotoImage(img_2_klein)
    img_2_label = tk.Label(frame_3)
    img_2_label.image = img_2_klein_fertig
    img_2_label['image'] = img_2_label.image
    img_2_label.pack(side=tk.LEFT)

    img_3 = Image.open(f"{eingabe_pfad}\{liste_bilder[2]}")
    img_3_klein = img_3.resize((100, 100))
    img_3_klein_fertig = ImageTk.PhotoImage(img_3_klein)
    img_3_label = tk.Label(frame_3)
    img_3_label.image = img_3_klein_fertig
    img_3_label['image'] = img_3_label.image
    img_3_label.pack(side=tk.LEFT)

    vorschau_info = tk.Label(text="""^^^ Hier ist eine Vorschau der Dateien, die sich in dem angegebenen Quellpfad befinden. Fahre fort, wenn es stimmt ^^^
    
    """)
    vorschau_info.pack()

    neu_starten_knopf_vorschau = tk.Button(
        text="Neu Starten",
        command=neu_starten_knopf_def,
        width=15
    )
    neu_starten_knopf_vorschau.pack()

    eingabe_pfadziel_def()


def eingabe_pfadziel_def():
    global pfad_ziel_text, pfadziel_eingabe_tk, Bestätigen_Zielpfad, knopf_gleiches_verzeichnis,\
        eingabe_pfadziel_gleich, pfadziel_eingabe_als_label
    if idiot == 2:
        leeres_label_2.config(fg="red", text=f"""
        
                        """)

    pfad_ziel_text = tk.Label(text="""
    
    Bitte kopiere den Dateipfad, in dem sich die Bilder nach der Sortierung befinden sollen, oder den Knopf, wenn sie im
    gleichen Verzeichis sortiert werden sollen, wo sie sich jetzt befinden!
    (Disclaimer: Bei falscher Angabe, könnte das Programm nicht funktionieren)""")
    pfad_ziel_text.pack()

    pfadziel_eingabe_tk = tk.Entry(
        width=50,
    )
    pfadziel_eingabe_tk.pack()

    pfadziel_eingabe_als_label = tk.Label(
        text=""
    )
    pfadziel_eingabe_als_label.pack()

    frame = tk.Frame(window)
    frame.pack()

    Bestätigen_Zielpfad = tk.Button(frame, width=15, text="Bestätigen", command=get_eingabe_zielpfad)
    Bestätigen_Zielpfad.pack(side=tk.LEFT)

    eingabe_pfadziel_gleich = 0

    knopf_gleiches_verzeichnis = tk.Button(frame, width=15, text="Gleiches Verzeichnis", command=gleiches_verzeichnis_def)
    knopf_gleiches_verzeichnis.pack(side=tk.LEFT)


def get_eingabe_zielpfad():
    global eingabe_pfadziel, foolproof_2
    foolproof_2 += 1
    if eingabe_pfadziel_gleich == 0:
        eingabe_pfadziel = pfadziel_eingabe_tk.get()
    print(eingabe_pfadziel)

    if foolproof_2 == 1:
        eingabe_zielpfad_bestätigt()
        kopieren_verschieben()


def eingabe_zielpfad_bestätigt():
    Bestätigen_Zielpfad.pack_forget()
    knopf_gleiches_verzeichnis.pack_forget()
    pfadziel_eingabe_tk.pack_forget()

    pfadziel_eingabe_als_label.config(fg="green", text=f"""
    \nAusgewählter Ziel-Pfad:{eingabe_pfadziel}""")
    pfadziel_eingabe_als_label.pack()


def gleiches_verzeichnis_def():
    global eingabe_pfadziel, eingabe_pfadziel_gleich
    if eingabe_pfadziel_gleich == 0:
        eingabe_pfadziel_gleich += 1
        eingabe_pfadziel = eingabe_pfad
        knopf_gleiches_verzeichnis.config(bg="green")
    else:
        eingabe_pfadziel_gleich -= 1
        knopf_gleiches_verzeichnis.config(bg="SystemButtonFace")


def kopieren_verschieben():
    global text_kov, frame, knopf_verschieben, knopf_kopieren
    text_kov = tk.Label(text="""
    Willst du die Bilder in die Ordner kopieren oder verschieben ?""")
    text_kov.pack()

    frame = tk.Frame(window)
    frame.pack()

    knopf_verschieben = tk.Button(frame,width=15, text="verschieben",command=verschieben_variable)
    knopf_verschieben.pack(side=tk.LEFT)

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
    global text_sortierung, knopf_sortieren_1, knopf_sortieren_2, knopf_sortieren_3, knopf_sortieren_4,\
        knopf_sortieren_5, knopf_sortieren_6, leeres_label, knopf_sortieren_bestätigen
    text_sortierung = tk.Label(text="""
    
    
    Wie willst du die Bilder sortieren ?""")
    text_sortierung.pack()

    knopf_sortieren_1 = tk.Button(
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
        text=">Bestätigen<",
        command=sortieren_bestätigt,
        width=15
    )
    knopf_sortieren_bestätigen.pack()


def sortieren_bestätigt():
    sortierung()
    end_screen()


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
    global keine_daten_text, knopf_erneut, leeres_label2, knopf_schließen
    center_window(window, 800, 325)

    neu_starten_def()

    if eingabe_kv == 1:
        kopiert_oder_verschoben = "kopiert"
    else:
        kopiert_oder_verschoben = "verschoben"

    if eingabe_sortierung == 1:
        so_sortiert = "Jahr > Beispielbild.png"
    elif eingabe_sortierung == 2:
        so_sortiert = "Jahr > Monat > Beispielbild.png"
    elif eingabe_sortierung == 3:
        so_sortiert = "Jahr > Monat > Tag > Beispielbild.png"
    elif eingabe_sortierung == 4:
        so_sortiert = "Jahr > Tag > Beispielbild.png"
    elif eingabe_sortierung == 5:
        so_sortiert = "Monat > Beispielbild.png"
    elif eingabe_sortierung == 6:
        so_sortiert = "Monat > Tag > Beispielbild.png"

    keine_daten_text = tk.Label(text=f"""
    Deine Bilder aus dem Pfad "{eingabe_pfad}" wurden in das Verzeichnis "{eingabe_pfadziel}", {kopiert_oder_verschoben}!
    Sie wurden in die Ordner, wie folgt sortiert: {so_sortiert}
    
    
    In {so_oft_keine_daten} Bildern wurde das DateTime Attribut nicht in den EXIF-Daten der Datei gefunden, sie wurden in den Ordner 'kein_datum' kopiert/verschoben.   
    """)
    keine_daten_text.pack()

    knopf_erneut = tk.Button(width=20, text="Weitere Bilder sortieren",command=neu_starten_knopf_def)
    knopf_erneut.pack()

    leeres_label2 = tk.Label(text="""
    
    
    
    
    
    """)
    leeres_label2.pack()

    knopf_schließen = tk.Button(width=20, text="Schließen", command=window.destroy)
    knopf_schließen.pack()


def end_screen_verschwinden():
    keine_daten_text.pack_forget()
    knopf_erneut.pack_forget()
    leeres_label2.pack_forget()
    knopf_schließen.pack_forget()

    main()


main()


window.mainloop()
