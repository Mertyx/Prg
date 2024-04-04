def prevod_hodin_na_dny_hodiny(hodiny):
    dny = hodiny // 24
    zbyvajici_hodiny = hodiny % 24
    return dny, zbyvajici_hodiny


hodiny = 56
dny, zbyvajici_hodiny = prevod_hodin_na_dny_hodiny(hodiny)
print(f"{hodiny} hodin je celkem {dny} dnů a {zbyvajici_hodiny} hodin.")