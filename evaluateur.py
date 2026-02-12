# module pour evaluer les mains de poker
from collections import Counter


def compter_rangs(cartes):
    # compte combien de fois chaque rang apparait
    compteur = Counter()
    for c in cartes:
        compteur[c.valeur()] += 1
    return compteur


def trouver_brelan(cartes):
    compteur = compter_rangs(cartes)
    brelans = [rang for rang, nb in compteur.items() if nb == 3]
    if len(brelans) == 1:
        rang_brelan = brelans[0]
        cartes_brelan = [c for c in cartes if c.valeur() == rang_brelan]
        kickers = sorted([c for c in cartes if c.valeur() != rang_brelan],
                         key=lambda c: c.valeur(), reverse=True)
        return cartes_brelan + kickers[:2]
    return None


def trouver_double_paire(cartes):
    compteur = compter_rangs(cartes)
    paires = sorted([rang for rang, nb in compteur.items() if nb == 2], reverse=True)
    if len(paires) == 2:
        paire_haute = paires[0]
        paire_basse = paires[1]
        cartes_haute = [c for c in cartes if c.valeur() == paire_haute]
        cartes_basse = [c for c in cartes if c.valeur() == paire_basse]
        kickers = sorted([c for c in cartes if c.valeur() != paire_haute and c.valeur() != paire_basse],
                         key=lambda c: c.valeur(), reverse=True)
        return cartes_haute + cartes_basse + kickers[:1]
    return None


def trouver_paire(cartes):
    compteur = compter_rangs(cartes)
    paires = [rang for rang, nb in compteur.items() if nb == 2]
    if len(paires) == 1:
        rang_paire = paires[0]
        cartes_paire = [c for c in cartes if c.valeur() == rang_paire]
        kickers = sorted([c for c in cartes if c.valeur() != rang_paire],
                         key=lambda c: c.valeur(), reverse=True)
        return cartes_paire + kickers[:3]
    return None


def evaluer_main(cartes):
    cartes_triees = sorted(cartes, key=lambda c: c.valeur(), reverse=True)

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
