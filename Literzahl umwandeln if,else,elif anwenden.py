'''1. Literzahl umwandeln
Es soll ein Programm implementiert werden, dass für beliebige Volumenangaben als
Gleitpunktzahl in Liter den entsprechenden Wert im ml, cl oder l ausgibt:
Eingabe Ausgabe
1.0 und größer l
0.1 und größer cl
0.001 und größer ml
kleiner als 0.001 Wert zu klein
Beispiel
Eingabe Ausgabe:
1.0 1.0 l
0.42 42.0 cl
0.023 23.0 ml
0.0001 Wert zu klein
'''

def umwandeln(volumen): 
    if volumen >=(volumen): 1.0:
        return f"{volumen} l"
    elif volumen >= 0.1:
        return f"{volumen*100} cl"
    elif volumen >= 0.001:
        return f"{volumen * 1000} ml"
    else: 
        return "Wert zu klein"

# Beispiele
print(umwandeln(1.0))    # 1.0 l
print(umwandeln(0.42))   # 42.0 cl
print(umwandeln(0.023))  # 23.0 ml
print(umwandeln(0.0001)) # Wert zu klein
