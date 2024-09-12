#Drei Eingaben von Namen, Geschlecht und Uhrzeit

name = input("Tragen Sie bitte ihren Namen ein  ")
geschlecht = input("Tragen Sie bitte ihr Geschlecht ein ")
uhrzeit = int(input("Tragen Sie bitte die Uhrzeit in Stunden ein "))

#Wenn Bedingung zutrifft, das mann ein Mann ist

if geschlecht == "Mann":
    if uhrzeit >= 0 and uhrzeit <= 9:
       print("Guten Morgen,Herr", name, "Es ist", uhrzeit, "Uhr")
    if uhrzeit >= 10 and uhrzeit <=17:
       print("Guten Tag,Herr", name, "Es ist", uhrzeit, "Uhr")
    if uhrzeit >= 18 and uhrzeit <= 23:
       print("Guten Abend,Herr", name, "Es ist", uhrzeit, "Uhr")

#Wenn Bedingung zutrifft das man eine Frau ist

if geschlecht == "Frau":
    if uhrzeit >= 0 and uhrzeit <= 9:
       print("Guten Morgen,Frau", name, "Es ist", uhrzeit, "Uhr")
    if uhrzeit >= 10 and uhrzeit <= 17:
       print("Guten Tag,Frau", name, "Es ist", uhrzeit, "Uhr")
    if uhrzeit >= 18 and uhrzeit <= 23:
       print("Guten Abend,Frau", name, "Es ist", uhrzeit, "Uhr")

#Wenn Bedingung zutrifft das man divers ist

if geschlecht == "divers":
    if uhrzeit >= 0 and uhrzeit <= 9:
       print("Guten Morgen", name, "Es ist", uhrzeit, "Uhr")
    if uhrzeit >= 10 and uhrzeit <= 17:
       print("Guten Tag", name, "Es ist", uhrzeit, "Uhr")
    if uhrzeit >= 18 and uhrzeit <= 23:
       print("Guten Abend", name, "Es ist", uhrzeit, "Uhr")

