''' Umdrehen von Zeichenketten, Listen und Tupeln:
Hier wird die Slicing Technik verwendet, um eine Kopie der Zeichenkette,
Liste oder des Tupels zu erstellen und die Elemente darin umzukehren.'''

def umgekehrte_elemente(reihenfolge):

# Beispiel
mein_string = "Guten Morgen, Schönheit!"
meine_liste = [1, 2, 3, 4, 5]
mein_tuple = (10, 20, 30, 40, 50)

print()
print(umgekehrte_elemente(mein_string)) # "teihöhcS, negroM netuG"
print()
print(umgekehrte_elemente(meine_liste)) # [5, 4, 3, 2, 1]
print(umgekehrte_elemente[mein_tuple)) # (50, 40, 30, 20, 10)

''' Umdrehen des Vorzeichens von Zahlen:
Hier wird eine Funktion geschrieben, die das Vorzeichen einer Zahl umkehrt.'''
def umgekehrtes_vorzeichen(zahl):
    return -zahl

# Beispiel
positive_zahl = 42
negative_zahl = -17.5

print(umgekehrtes_vorzeichen(postive_zahl)) # -42
print(umgekehrtes_vorzeichen(negative_zahl)) # 17.5
print()

''' Testen der Funktionen:
Hier werden die Testdaten für verschiedene Datentypen erstellt und die Funkionen darauf angewendet.'''
# Testdaten
mein_string = "Gute Nacht, lieber Mond!"
meine_liste = [1, 2, 3, 4, 5]
mein_tuple = (10, 20, 30. 40, 50)
mein_positiver_wert = 42
mein_negativer_wert = -17.5

# Anwenden der Funktionen
print(umgekehrte_elemente(mein_string))
print()
print(umgekehrte_elemente(meine_liste))
print(umgekehrte_elemente(mein_tuple))
print(umgekehrtes_vorzeichen(mein_positiver_wert))
print(umgekehrtes_vorzeichen(meine_negativer_wert))


