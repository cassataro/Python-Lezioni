lista_1 = [1, 10, 15, 20, 1, 10, 15, 20, 25]

print(lista_1)

# stampa il secondo nella lista
print(lista_1[1])

# cambiando il valore del terzo nella lista
lista_1[2] = 10
print(lista_1)

# Stampare i primi 3 elementi della lista
print(lista_1[:3])

# Rimuovere il 2 elemento della lista
del lista_1[1]
print(lista_1)

# Contare quante volte un elemento è presente nella lista
conteggio_lista = lista_1.count(1)
print(conteggio_lista)