ore_lavorative = float(input("Quante ore lavorative effettui durante il giorno? "))
tariffa_oraria = float(input("Quale è la tua tariffa oraria? "))
tariffa_giornaliera = float(tariffa_oraria) * float(ore_lavorative)
paga_lorda = float(tariffa_giornaliera) * 7


print ("Con il tuo lavoro hai guadagnato " + str(paga_lorda) + " € a settimana" )