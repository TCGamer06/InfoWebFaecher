import os  # renamen von dateien
import webbrowser  # Oeffnen der html file automatisch
import glob  # alle dateien mit stylesheet im namen auslesen
import pathlib  # Liest __file__ in der der Aktuell durchs Skript genutzte Dateipfad steht
import platform  # liest betriebsystem aus


def get_style():
    result = glob.glob('stylesheet*.css')  # Weißt Liste alle namen von dateien mit stylesheet
    for filename in result:  # Loopt durch Result
        with open(filename, "r") as file:  # Oeffnet File zum lesen die gerade geloopt wird und schließt sie nach folgendem Prozess wieder
            color = file.readlines()[0].replace("\n", "").replace(" ", "")  # Liest erste Zeile schreibt sie in Variable und löscht Zeilenumbruch und Leerzeichen
        yield color  # Gibt ALLE erste Zeilen als Generator zurück


def reset_stylesheets():
    result = glob.glob('stylesheet*.css')  # Weißt Variable alle namen von dateien mit stylesheet... als Liste zu  Gleich zu get_style()
    for filename in result:  # ""
        with open(filename, "r") as file:  # ""
            color = file.readlines()[0].replace("\n", "").replace(" ", "")  # ""
        os.rename(filename, f"stylesheet-{color}.css")  # Renamed gerade geloopte File zu der zugewiesenen Color

def main():
    colors = list(get_style())  # Gibt Generator als Liste zu einer Variable
    questionstring = "Colorscheme("  # Neue Var mit String
    for target in colors:  # Looped durch Colors
        questionstring += target + ", "  # Fügt zu Var die geloopte Color und ", " hinzu
    questionstring = questionstring[:-2] + "): "  # Löscht das letzte unnötige ", " und fügt zum Schluss noch "): " hinzu
    abfrage = input(questionstring)  # User Input
    reset_stylesheets()  # Führt Function aus
    os.rename(f"stylesheet-{abfrage.lower()}.css", "stylesheet.css")  # Renamed gewünschten Style zu stylesheet.css das es in jeder HTML-File verlinkt ist
    directory_path = pathlib.Path(__file__).parent.resolve()  # Liest durch pathlib Var __file__ in der der Dateipfad der gerade aktiven Datei steht und weist sie einer Variable zu
    opsys = platform.system()  # Gibt Variable Betriebssystem an
    if opsys == "Windows":  # Wenn Betriebsystem Windows:
        webbrowser.open_new_tab(f"{directory_path}\\homepage\\Homepage.html")  # Öffnet neuen Browser Tab im Standart Browser mit Windows Filepath für Homepage
    else:
        webbrowser.open_new_tab(f"{directory_path}/homepage/Homepage.html")  # Öffnet neuen Browser Tab im Standart Browser mit Linux/Mac Filepath für Homepage


if __name__ == "__main__":  # Führt main() aus
    main()
