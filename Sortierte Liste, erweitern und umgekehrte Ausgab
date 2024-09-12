# Erstelle sortierte Liste von Großstädten, anschließend zwei weitere Städte hinzufügen, sortieren und abschließend in umgekehrter Reihenfolge ausgeben

def main():
    # Erstelle eine Liste mit fünf Großstädten
    grossstaedte = ["Berlin", "München", "Hamburg", "Köln", "Frankfurt"]

    # Sortiere die Liste
    grossstaedte.sort()
    print("Sortierte Liste der Großstädte:")
    print(grossstaedte)

    # Füge zwei weitere Städte hinzu
    stadt1 = input("Gib den Namen einer weiteren Stadt ein: ")
    stadt2 = input("Gib den Namen einer zweiten Stadt ein: ")
    grossstaedte.extend([stadt1, stadt2])

    # Sortiere die erweiterte Liste
    grossstaedte.sort()
    print("\nSortierte Liste mit 7 Städten:")
    print(grossstaedte)

    # Gib die Liste in umgekehrter Reihenfolge aus
    print("\nListe in umgekehrter Reihenfolge:")
    print(grossstaedte[::-1])

    # Entferne die erste und letzte Stadt
    grossstaedte.pop(0)
    grossstaedte.pop(-1)

    # Gib die reduzierte Liste aus
    print("\nReduzierte Liste:")
    print(grossstaedte)

if __name__ == "__main__":
    main()
