nome_utente = input("Quale è il tuo nome? ")
eta_utente = int(input("Quanti anni hai? "))
if eta_utente < 18:
    print("Ti diamo il benvenuto" , nome_utente , "! Sei un minorenne.")
if eta_utente > 18:
    print("Ti diamo il benvenuto" , nome_utente , "! Sei un maggiorenne.")

print ("")

password_sicura = int(input("Inserisci la tua password "))
if password_sicura == 1234:
    print ("Benvenuto" , nome_utente)
else:
    print("Password non corretta")

print ("")