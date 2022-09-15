ore_lavorative = float(input("Inserisci le tue ore lavorative: "))
tariffa_oraria = int(10)
ore_straordinario = int(15)
if ore_lavorative == 40:
    paga_totale = ore_lavorative * tariffa_oraria
    print("Ore lavorative:" , ore_lavorative)
    print("Tariffa Oraria: 10")
    print("Paga totale:" , paga_totale)
print("")

if ore_lavorative < 40:
    paga_totale = ore_lavorative * tariffa_oraria
    print("Ore lavorative:" , ore_lavorative)
    print("Tariffa Oraria: 10")
    print("Paga totale:" , paga_totale)
print("")

if ore_lavorative > 40:
    paga_totale = ore_lavorative * ore_straordinario
    print("Ore lavorative:" , ore_lavorative)
    print("Tariffa Oraria: 15")
    print("Paga totale:" , paga_totale)
print("")