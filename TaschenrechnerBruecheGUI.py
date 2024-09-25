'''Erklärung des Codes:
Importieren der Bibliothek: from tkinter import * importiert alle notwendigen Funktionen und Klassen aus der tkinter-Bibliothek.
Hauptfenster: tk_fenster = Tk() erstellt das Hauptfenster der Anwendung.
Eingabefelder: Zwei Eingabefelder (Entry) werden erstellt, um die Brüche einzugeben.
Buttons: Vier Buttons (+, -, *, /) werden erstellt, um die Operationen auszuführen.
Berechnungsfunktion: Die Funktion berechne(operation) führt die gewählte mathematische Operation aus und zeigt das Ergebnis an.
Ergebnisanzeige: Das Ergebnis wird in einem Label (lb_ergebnis) angezeigt.
Hauptschleife: tk_fenster.mainloop() startet die Hauptschleife der GUI-Anwendung.'''

from tkinter import *
from fractions import Fraction

# Funktion zur Berechnung
def berechne(operation):
    try:
        bruch1 = Fraction(ent_bruch_1.get())
        bruch2 = Fraction(ent_bruch_2.get())
        
        if operation == "fl":
            ergebnis = f"{float(bruch1):.3f}"
        else: 
            
            if operation == "+":
                ergebnis = bruch1 + bruch2
            elif operation == "-":
                ergebnis = bruch1 - bruch2
            elif operation == "*":
                ergebnis = bruch1 * bruch2
            elif operation == "/":
                ergebnis = bruch1 / bruch2
        
        
            # Bruch vereinfachen, wenn möglich
            ergebnis = ergebnis.limit_denominator(1000)  # Anpassbare maximale Zahl im Nenner
        lb_ergebnis.config(text=str(ergebnis))
    except ValueError:
        lb_ergebnis.config(text="Ungültige Eingabe")
        
# Hauptfenster
tk_fenster = Tk()
tk_fenster.title("Bruch Rechner")

# Eingabeframe
frm_eingabe = Frame(tk_fenster, bg="#f0f0f0")
frm_eingabe.pack(padx=10, pady=10)

# Bruch 1
frm_bruch_1 = Frame(frm_eingabe, bg="#f0f0f0")
frm_bruch_1.pack(side="left", padx=5, pady=5)
Label(frm_bruch_1, text="Bruch 1", font=("Arial", 12)).pack(padx=5, pady=5)
ent_bruch_1 = Entry(frm_bruch_1, width=20, font=("Arial", 12))
ent_bruch_1.pack(padx=5, pady=5)

# Bruch 2
frm_bruch_2 = Frame(frm_eingabe, bg="#f0f0f0")
frm_bruch_2.pack(side="right", padx=5, pady=5)
Label(frm_bruch_2, text="Bruch 2", font=("Arial", 12)).pack(padx=5, pady=5)
ent_bruch_2 = Entry(frm_bruch_2, width=20, font=("Arial", 12))
ent_bruch_2.pack(padx=5, pady=5)

# Buttonframe
frm_btn = Frame(tk_fenster, bg="#f0f0f0")
frm_btn.pack(padx=10, pady=10)

# Buttons
btn_style = {"font": ("Arial", 12), "cursor": "hand2", "width": 5, "height": 2, "bg": "#4CAF50", "fg": "white"}
Button(frm_btn, text="+", **btn_style, command=lambda: berechne("+")).pack(side="left", padx=5, pady=5)
Button(frm_btn, text="-", **btn_style, command=lambda: berechne("-")).pack(side="left", padx=5, pady=5)
Button(frm_btn, text="*", **btn_style, command=lambda: berechne("*")).pack(side="left", padx=5, pady=5)
Button(frm_btn, text="/", **btn_style, command=lambda: berechne("/")).pack(side="left", padx=5, pady=5)
Button(frm_btn, text="fl", **btn_style, command=lambda: berechne("fl")).pack(side="left", padx=5, pady=5)

# Ausgabeframe
frm_ausgabe = Frame(tk_fenster, bg="#7cfc00")
frm_ausgabe.pack(padx=10, pady=10)
Label(frm_ausgabe, text="Ergebnis", font=("Arial", 12)).pack()
lb_ergebnis = Label(frm_ausgabe, text="", font=("Arial", 12), 
                        relief="groove", borderwidth=2, bg="#ffffff") #Diese beiden Parameter zusammen erzeugen eine Umrandung um das Label, die das Ergebnis anzeigt.
lb_ergebnis.pack(padx=5, pady=5)

# Hauptschleife
tk_fenster.mainloop()
