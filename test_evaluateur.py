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
