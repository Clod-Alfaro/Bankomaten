'''VISA MENY A
   1. Skapa konto
   2. Logga in på konto
   3. Avsluta
           1. Skapa konto
             - Input ange kontonummer
             - Om redan taget "Felmeddelande"
             - Annars skapa och tillbaka till meny A
           2. Logga in på konto
             - Input ange kontonummer
             - Om ej finns "Felmeddelande"
             - Annars OK och gå till meny   
VISA MENY B
   - Ta ut pengar.   if bankomaten har 20 kr.  
   - Sätt in pengar  
   - Visa saldo
           TA UT PENGAR
                   - Input ange belopp
                   - Om belopp > saldo "Felmeddelande"
                   - Annars ok och gå till meny B
           SÄTT IN PENGAR
                   - Input ange belopp
                   - Öka saldo och tillbaka till meny B
           VISA SALDO
                   - Skriv ut aktuellt saldo '''


def skapaNyKonto ():
    print("_______________________\nSKAPA KONTO:\n_______________________\nSkapa ny kund. ")              
    namn = input("Ange namn på kunden: ")      
def administreraKonto ():
    print("ADMINISTRERA KONTO:\nSök kund: ")            
    namn = input("Sök efter i namn")                      

while True:    
    print("      HUVUDMENY      ")
    print("_______________________")
    print("1. SKAPA KONTO")
    print("_______________________")
    print("2. ADMINISTRERA KONTO")
    print("_______________________")
    print("3. LOGGA UT")
    print("_______________________")
   
    selection = int(input())
    if selection == 1:
           skapaNyKonto ()
    elif selection == 2:
           administreraKonto ()
    elif selection == 3:
           print("Du är nu utloggat.\nTack och välkommen åter!\n______________________")
    
      
    print("")

