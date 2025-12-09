import json

def ikelti_kontaktus():
    global kontaktai
    try:
        with open("kontaktai.json", "r") as f:
            kontaktai = json.load(f)
    except:
        kontaktai = []

def issaugoti_kontaktus():
    with open("kontaktai.json", "w") as f:
        json.dump(kontaktai, f, indent=4)

def prideti_kontakta():
    vardas = input("Įveskite vardą: ")
    tel = input("Įveskite telefono numerį: ")

    kontaktas = {
        "vardas": vardas,
        "tel": tel
    }
    kontaktai.append(kontaktas)
    print("Kontaktas pridėtas!")

def rodyti_kontaktus():
    if len(kontaktai) == 0:
        print("Kontaktų sąrašas tuščias.")
    else:
        print("\n--- Kontaktų sąrašas ---")
        for kontaktas in kontaktai:
            print("Vardas:", kontaktas["vardas"], "| Tel:", kontaktas["tel"])

def istrinti_kontakta():
    vardas = input("Įveskite vardą, kurį norite ištrinti: ")
    for kontaktas in kontaktai:
        if kontaktas["vardas"] == vardas:
            kontaktai.remove(kontaktas)
            print("Kontaktas ištrintas!")
            return
    print("Toks kontaktas nerastas.")

ikelti_kontaktus()

while True:
    print("\n=== KONTAKTŲ VALDYMO SISTEMA ===")
    print("1 - Pridėti kontaktą")
    print("2 - Rodyti kontaktus")
    print("3 - Ištrinti kontaktą")
    print("4 - Išeiti")

    pasirinkimas = input("Pasirinkite: ")

    if pasirinkimas == "1":
        prideti_kontakta()
    elif pasirinkimas == "2":
        rodyti_kontaktus()
    elif pasirinkimas == "3":
        istrinti_kontakta()
    elif pasirinkimas == "4":
        issaugoti_kontaktus()
        print("Kontaktai sėkmingai išsaugoti. Viso gero!")
        break
    else:
        print("Neteisingas pasirinkimas!")
