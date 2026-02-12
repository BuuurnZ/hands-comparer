# module pour evaluer les mains de poker
from collections import Counter


def compter_rangs(cartes):
    # compte combien de fois chaque rang apparait
    compteur = Counter()
    for c in cartes:
        compteur[c.valeur()] += 1
    return compteur


def filtrer_par_valeur(cartes, valeur):
    # retourne les cartes qui ont la valeur donnee
    return [c for c in cartes if c.valeur() == valeur]


def kickers_tries(cartes, valeurs_exclues):
    # retourne les kickers tries par valeur decroissante
    # en excluant les valeurs donnees
    return sorted([c for c in cartes if c.valeur() not in valeurs_exclues],
                  key=lambda c: c.valeur(), reverse=True)


def trouver_brelan(cartes):
    compteur = compter_rangs(cartes)
    brelans = [rang for rang, nb in compteur.items() if nb == 3]
    if len(brelans) == 1:
        rang_brelan = brelans[0]
        return filtrer_par_valeur(cartes, rang_brelan) + kickers_tries(cartes, [rang_brelan])[:2]
    return None


def trouver_double_paire(cartes):
    compteur = compter_rangs(cartes)
    paires = sorted([rang for rang, nb in compteur.items() if nb == 2], reverse=True)
    if len(paires) == 2:
        paire_haute = paires[0]
        paire_basse = paires[1]
        return filtrer_par_valeur(cartes, paire_haute) + filtrer_par_valeur(cartes, paire_basse) + kickers_tries(cartes, [paire_haute, paire_basse])[:1]
    return None


def trouver_paire(cartes):
    compteur = compter_rangs(cartes)
    paires = [rang for rang, nb in compteur.items() if nb == 2]
    if len(paires) == 1:
        rang_paire = paires[0]
        return filtrer_par_valeur(cartes, rang_paire) + kickers_tries(cartes, [rang_paire])[:3]
    return None


def trouver_couleur(cartes):
    # verifie si toutes les cartes ont la meme couleur
    couleurs = [c.couleur for c in cartes]
    if len(set(couleurs)) == 1:
        return sorted(cartes, key=lambda c: c.valeur(), reverse=True)
    return None


def est_suite_normale(valeurs):
    # verifie si les valeurs forment une suite normale (sans trou)
    return len(set(valeurs)) == 5 and valeurs[0] - valeurs[4] == 4


def est_wheel(valeurs):
    # verifie si c'est un wheel (A-2-3-4-5)
    return set(valeurs) == {14, 2, 3, 4, 5}


def ordonner_wheel(cartes):
    # ordonne les cartes du wheel : 5, 4, 3, 2, A
    resultat = []
    for v in [5, 4, 3, 2, 14]:
        for c in cartes:
            if c.valeur() == v and c not in resultat:
                resultat.append(c)
                break
    return resultat


def trouver_suite(cartes):
    cartes_triees = sorted(cartes, key=lambda c: c.valeur(), reverse=True)
    valeurs = [c.valeur() for c in cartes_triees]

    if est_suite_normale(valeurs):
        return cartes_triees

    if est_wheel(valeurs):
        return ordonner_wheel(cartes)

    return None


def evaluer_main(cartes):
    cartes_triees = sorted(cartes, key=lambda c: c.valeur(), reverse=True)

    # verifier couleur (flush)
    resultat_couleur = trouver_couleur(cartes)
    if resultat_couleur is not None:
        return {
            "categorie": "couleur",
            "chosen5": resultat_couleur,
        }

    # verifier suite
    resultat_suite = trouver_suite(cartes)
    if resultat_suite is not None:
        return {
            "categorie": "suite",
            "chosen5": resultat_suite,
        }

    # verifier brelan
    resultat_brelan = trouver_brelan(cartes)
    if resultat_brelan is not None:
        return {
            "categorie": "brelan",
            "chosen5": resultat_brelan,
        }

    # verifier double paire
    resultat_dp = trouver_double_paire(cartes)
    if resultat_dp is not None:
        return {
            "categorie": "double paire",
            "chosen5": resultat_dp,
        }

    # verifier paire
    resultat_paire = trouver_paire(cartes)
    if resultat_paire is not None:
        return {
            "categorie": "paire",
            "chosen5": resultat_paire,
        }

    return {
        "categorie": "carte haute",
        "chosen5": cartes_triees[:5],
    }
