ore_lavorative = float(input("Inserisci le tue ore lavorative: "))
tariffa_oraria = int(10)
ore_straordinario = tariffa_oraria * 1.5
if ore_lavorative == 40:
    paga_totale = ore_lavorative * tariffa_oraria
    print("Ore lavorative:", ore_lavorative)
    print("Tariffa Oraria:", tariffa_oraria)
    print("Paga totale:", paga_totale)

if ore_lavorative < 40:
    paga_totale = ore_lavorative * tariffa_oraria
    print("Ore lavorative:", ore_lavorative)
    print("Tariffa Oraria:", tariffa_oraria)
    print("Paga totale:", paga_totale)

if ore_lavorative > 40:
    paga_totale = ore_lavorative * ore_straordinario
    print("Ore lavorative:", ore_lavorative)
    print("Tariffa Oraria:", ore_straordinario)
    print("Paga totale:", paga_totale)
