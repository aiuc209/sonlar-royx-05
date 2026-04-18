import math

def logarifm_royxati(sonlar):
    natija = []
    for son in sonlar:
        if son < 0:
            son = -son
        natija.append(math.log(son))
    return natija

sonlar = [1, -2, 3, -4, 5]
print(logarifm_royxati(sonlar))
