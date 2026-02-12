# module pour evaluer les mains de poker
from collections import Counter


def compter_rangs(cartes):
    # compte combien de fois chaque rang apparait
    compteur = Counter()
    for c in cartes:
        compteur[c.valeur()] += 1
    return compteur


def trouver_paire(cartes):
    compteur = compter_rangs(cartes)
    paires = [rang for rang, nb in compteur.items() if nb == 2]
    if len(paires) == 1:
        rang_paire = paires[0]
        # on met la paire en premier puis les kickers decroissants
        cartes_paire = [c for c in cartes if c.valeur() == rang_paire]
        kickers = sorted([c for c in cartes if c.valeur() != rang_paire],
                         key=lambda c: c.valeur(), reverse=True)
        return cartes_paire + kickers[:3]
    return None


def evaluer_main(cartes):
    cartes_triees = sorted(cartes, key=lambda c: c.valeur(), reverse=True)

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
