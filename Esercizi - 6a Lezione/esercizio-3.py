print('Indovina un numero tra 1 e 100')

# Si comunica all'utente seil numero inserito è "troppo grande” o “troppo piccolo” rispetto a quello misterioso
while True:
    numero_utente = int(input("Dammi un numero: "))
    if numero_utente in range(1, 58):
        print('Il numero è troppo piccolo, Ritenta!')
    if numero_utente in range(59, 101):
        print('Il numero è troppo grande, Ritenta!')
    if numero_utente > 101:
        print('Il numero non è tra 1 e 100, Ritenta!')
    if numero_utente == 58:
        break

print("Complimeti hai vinto!")
