# pouze ukázkové zadání
mocnenec = 3.14 mocnitel = 5
# proveď „umocňování“
vysledek = mocnenec
for i in range(mocnitel-1):
vysledek *= mocnenec
# vypiš výsledek
txt = "Výsledek: {0}^{1} = {2}".format(mocnenec, mocnitel, vysledek)
print( txt )