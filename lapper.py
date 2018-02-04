import random


def lag_lapper(antall_lapper, antall_kryss):
    return [True]*antall_kryss+[False]*(antall_lapper-antall_kryss)


def trekk_lapp(lapper):
    lapp = random.choice(lapper)
    lapper.remove(lapp)
    return lapp


def trekk_n_lapper(antall_lapper, antall_kryss, antall_trekninger):

    lapper = lag_lapper(antall_lapper, antall_kryss)
    trekte_lapper = []

    for i in range(antall_trekninger):
        trekte_lapper.append(trekk_lapp(lapper))

    return trekte_lapper


def main():
    resultat = []
    for i in range(20):                                         # Gjenta følgende 20 ganger:
        trekte_lapper = trekk_n_lapper(100, 50, 10)                  # Trekk 10 lapper fra 100, der 50 har kryss.
        antall_trekte_kryss = sum(i is True for i in trekte_lapper)  # Summer opp hvor mange kryss vi trakk.
        resultat.append(antall_trekte_kryss)                         # Legg til antall trekte kryss i resultat-lista.

    print(resultat)

if __name__ == '__main__':
    main()
