primo_numero = int(input("Dammi un numero: "))
secondo_numero = int(input("Dammi un secondo numero: "))

# Stampa il numero binario
print("Il numero binario di", primo_numero, "é:", bin(primo_numero))
print("Il numero binario di", secondo_numero, "é:", bin(secondo_numero))

# Restituisce una coppia di numeri (una tupla) composta dal loro quoziente e dal resto
print("La tupla dei due numeri è:", divmod(primo_numero, secondo_numero))

# restituisce un numero con la virgola
print("La somma dei due numeri è:", float(primo_numero + secondo_numero))
