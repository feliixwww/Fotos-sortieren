## Vor dem Start

- Damit das Programm funktioniert, werden die Module "pillow" und "pathlib" benötigt
- Diese lassen sich im Terminal mit "pip install pillow" und "pip install pathlib" installieren
- Möglicherweise musst du dafür erst noch "pip" installieren, was mit "easyinstall pip" gemacht wird


## Auswahl der Quelle

- Zuerst wird dich das Programm fragen, in welchem Dateipfad sich die Bilder, die sortiert werden sollen befinden
- Den Pfad kann man ganz leicht kopieren, indem man im Dateiexplorer, die Leiste, links von der Suche, rechtsklickt
und dann auf "Adresse kopieren" drückt.
- Achten sie darauf, im eingabefeld keine Leerzeile, oder andere Zeichen, an den Pfad zu schreiben, da dies zu fehlern
im Programm führen kann

## Auswahl des Ziels

- Das gleiche Prozedere gilt auch beim auswählen des Zielordners im Anschluss, hier gibt es aber, um Zeit zu sparen
auch die Option, nur eine "1" zu schreiben, wodurch die sortierten Ordner in dem Verzeichnis erstellt werden, wo sich
deine Bilder, laut der vorher gemachten Angabe, zurzeit befinden

## Kopieren oder verschieben?

- Nun zeigt das Programm die namen einiger Bilddateien an, such dir am besten ein paar aus und überprüfe, ob der
dateipfad die richtigen Bilder enthält, da es sonst ziemlich mühselig werden könnte, vor allem, nachdem man verschoben
hat, die Dateien aus den Ordnern wieder herauszuholen
- Wie bereits erwähnt gibt es jetzt die Option, die Bilder entweder zu kopieren, oder zu verscieben, wähle deine
Bevorzugte Methode mit "1" zum kopieren oder "2" zum verschieben aus

## Zeitstrukturierung

- Nun lässt sich auswählen, wie die Bilder sortiert werden sollen
___
- Bei `1` werden die Bilder nur nach Jahren sortiert
- Beispiel: 2015 > Bild.png
___
- Bei `2` werden zudem Ordner mit den Namen der Monate in den Jahresordnern erstellt
- Beispiel: 2016 > 08_August > Bild.png
___
- Bei `3` gibt es in den Jahr-Ordnern, die Monate und darin, jeweils die Tage
- Beispiel: 2017 > 09_September > 04 > Bild.png
___
- Bei `4` werden die Ordner im Jahr-Ordner, mit Monaten und Tagesangaben erstellt
- Beispiel: 2018 > 10_Oktober der_06te > Bild.png
___
- Bei `5` werden die Bilder nur in Order, der jeweiligen Monate sortiert
- Beispiel: 11_November > Bild.png
___
- Bei `6` werden die Bilder in ordner der jeweiligen Monate, sowie darunter Tage sortiert
- Beispiel: 12_Dezember > 08 > Bild.png

## Fehlermeldung

- Falls ein Bild in den EXIF-Daten kein Datum hat, wird dieses in einen extra Ordner mit dem Namen "kein_datum" kopiert
oder verschoben, da es sonst keinem Ordner zugeordnet werden kann