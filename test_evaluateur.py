# tests pour l'evaluateur de mains de poker
from carte import Carte
from evaluateur import evaluer_main


def test_high_card_basique():
    main = [
        Carte("A", "pique"),
        Carte("K", "coeur"),
        Carte("9", "carreau"),
        Carte("7", "trefle"),
        Carte("3", "pique"),
    ]
    resultat = evaluer_main(main)
    assert resultat["categorie"] == "carte haute"


def test_high_card_chosen5():
    main = [
        Carte("A", "pique"),
        Carte("K", "coeur"),
        Carte("9", "carreau"),
        Carte("7", "trefle"),
        Carte("3", "pique"),
    ]
    resultat = evaluer_main(main)
    # les 5 cartes doivent etre triees par rang decroissant
    valeurs = [c.valeur() for c in resultat["chosen5"]]
    assert valeurs == [14, 13, 9, 7, 3]


def test_high_card_ordre_decroissant():
    main = [
        Carte("Q", "pique"),
        Carte("10", "coeur"),
        Carte("8", "carreau"),
        Carte("5", "trefle"),
        Carte("2", "pique"),
    ]
    resultat = evaluer_main(main)
    assert resultat["categorie"] == "carte haute"
    valeurs = [c.valeur() for c in resultat["chosen5"]]
    assert valeurs == [12, 10, 8, 5, 2]


# --- tests pour une paire ---

def test_une_paire_basique():
    main = [
        Carte("A", "pique"),
        Carte("A", "coeur"),
        Carte("K", "carreau"),
        Carte("7", "trefle"),
        Carte("3", "pique"),
    ]
    resultat = evaluer_main(main)
    assert resultat["categorie"] == "paire"


def test_une_paire_chosen5():
    main = [
        Carte("10", "pique"),
        Carte("10", "coeur"),
        Carte("K", "carreau"),
        Carte("7", "trefle"),
        Carte("3", "pique"),
    ]
    resultat = evaluer_main(main)
    assert resultat["categorie"] == "paire"
    # la paire d'abord, puis kickers decroissants
    valeurs = [c.valeur() for c in resultat["chosen5"]]
    assert valeurs == [10, 10, 13, 7, 3]


def test_une_paire_basse():
    main = [
        Carte("2", "pique"),
        Carte("2", "coeur"),
        Carte("A", "carreau"),
        Carte("K", "trefle"),
        Carte("Q", "pique"),
    ]
    resultat = evaluer_main(main)
    assert resultat["categorie"] == "paire"
    valeurs = [c.valeur() for c in resultat["chosen5"]]
    assert valeurs == [2, 2, 14, 13, 12]
