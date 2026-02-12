# module pour evaluer les mains de poker


def evaluer_main(cartes):
    # pour l'instant on gere juste la carte haute
    # on trie les cartes par valeur decroissante
    cartes_triees = sorted(cartes, key=lambda c: c.valeur(), reverse=True)

    return {
        "categorie": "carte haute",
        "chosen5": cartes_triees[:5],
    }
