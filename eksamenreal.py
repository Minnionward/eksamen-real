from pymongo import MongoClient

# Koble til MongoDB-serveren ved hjelp av en MongoDB Atlas-URI
klient = MongoClient('mongodb+srv://Minionward:czQmUj28yr9kR9S@cluster0.szjwecp.mongodb.net/')
db = klient['bussturer']  # Velg databasen 'bussturer'
turer_samling = db['turer']  # Velg eller opprett samlingen 'turer'
passasjerer_samling = db['passasjerer']  # Velg eller opprett samlingen 'passasjerer'

def registrer_tur():
    """Funksjon for å registrere en ny tur."""
    tur_navn = input("Skriv inn navnet på turen: ")  # Be om navnet på turen
    turer_samling.insert_one({'navn': tur_navn})  # Sett inn turen i databasen
    print(f"Turen '{tur_navn}' er registrert.")  # Bekreftelse til brukeren

def registrer_passasjer():
    """Funksjon for å registrere en ny passasjer."""
    fornavn = input("Skriv inn fornavn: ")  # Be om passasjerens fornavn
    etternavn = input("Skriv inn etternavn: ")  # Be om passasjerens etternavn
    tur_navn = input("Skriv inn navnet på turen de skal delta på: ")  # Be om turens navn
    
    # Sjekk om turen eksisterer i databasen
    tur = turer_samling.find_one({'navn': tur_navn})
    if tur:
        # Sett inn passasjeren i databasen hvis turen eksisterer
        passasjerer_samling.insert_one({
            'fornavn': fornavn,
            'etternavn': etternavn,
            'tur_navn': tur_navn
        })
        print(f"{fornavn} {etternavn} er registrert på turen '{tur_navn}'.")  # Bekreftelse til brukeren
    else:
        print(f"Turen '{tur_navn}' eksisterer ikke. Vennligst registrer turen først.")  # Feilmelding hvis turen ikke finnes

def list_turer():
    """Funksjon for å vise en oversikt over alle turer."""
    turer = turer_samling.find()  # Hent alle turer fra databasen
    print("Oversikt over alle turer:")  # Overskrift
    for tur in turer:
        print(f"- {tur['navn']}")  # Skriv ut navnet på hver tur

def list_passasjerer():
    """Funksjon for å vise en oversikt over alle påmeldte passasjerer."""
    passasjerer = passasjerer_samling.find()  # Hent alle passasjerer fra databasen
    print("Oversikt over alle påmeldte:")  # Overskrift
    for passasjer in passasjerer:
        # Skriv ut navn og tilhørende tur for hver passasjer
        print(f"- {passasjer['fornavn']} {passasjer['etternavn']} (Tur: {passasjer['tur_navn']})")

def hovedmeny():
    """Hovedmeny for å navigere mellom forskjellige funksjoner."""
    while True:
        # Skriv ut menyen med alternativer
        print("\nMeny:")
        print("1. Registrer ny tur")
        print("2. Registrer ny passasjer")
        print("3. Vis oversikt over alle turer")
        print("4. Vis oversikt over alle påmeldte")
        print("5. Avslutt")
        valg = input("Velg et alternativ: ")  # Be brukeren velge et alternativ
        
        # Utfør handling basert på brukerens valg
        if valg == '1':
            registrer_tur()
        elif valg == '2':
            registrer_passasjer()
        elif valg == '3':
            list_turer()
        elif valg == '4':
            list_passasjerer()
        elif valg == '5':
            print("Avslutter programmet.")  # Avslutt programmet
            break
        else:
            print("Ugyldig valg, prøv igjen.")  # Feilmelding for ugyldig valg

if __name__ == "__main__":
    hovedmeny()  # Start hovedmenyen
