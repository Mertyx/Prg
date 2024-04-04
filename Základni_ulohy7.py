def prevod_dni_na_hodiny(dny, hodiny):
    pocet_hodin = dny * 24 + hodiny
    return pocet_hodin

dny = 7
hodiny = 8
vysledek = prevod_dni_na_hodiny(dny, hodiny)
print(f"{dny} dní a {hodiny} hodin je celkem {vysledek} hodin.")