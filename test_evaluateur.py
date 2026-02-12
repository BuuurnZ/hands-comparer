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


# --- tests pour double paire ---

def test_double_paire_basique():
    main = [
        Carte("A", "pique"),
        Carte("A", "coeur"),
        Carte("K", "carreau"),
        Carte("K", "trefle"),
        Carte("3", "pique"),
    ]
    resultat = evaluer_main(main)
    assert resultat["categorie"] == "double paire"


def test_double_paire_chosen5():
    main = [
        Carte("J", "pique"),
        Carte("J", "coeur"),
        Carte("5", "carreau"),
        Carte("5", "trefle"),
        Carte("A", "pique"),
    ]
    resultat = evaluer_main(main)
    assert resultat["categorie"] == "double paire"
    # paire haute, paire basse, kicker
    valeurs = [c.valeur() for c in resultat["chosen5"]]
    assert valeurs == [11, 11, 5, 5, 14]


def test_double_paire_petites():
    main = [
        Carte("3", "pique"),
        Carte("3", "coeur"),
        Carte("2", "carreau"),
        Carte("2", "trefle"),
        Carte("7", "pique"),
    ]
    resultat = evaluer_main(main)
    assert resultat["categorie"] == "double paire"
    valeurs = [c.valeur() for c in resultat["chosen5"]]
    assert valeurs == [3, 3, 2, 2, 7]


# --- tests pour brelan ---

def test_brelan_basique():
    main = [
        Carte("7", "pique"),
        Carte("7", "coeur"),
        Carte("7", "carreau"),
        Carte("K", "trefle"),
        Carte("3", "pique"),
    ]
    resultat = evaluer_main(main)
    assert resultat["categorie"] == "brelan"


def test_brelan_chosen5():
    main = [
        Carte("Q", "pique"),
        Carte("Q", "coeur"),
        Carte("Q", "carreau"),
        Carte("A", "trefle"),
        Carte("9", "pique"),
    ]
    resultat = evaluer_main(main)
    assert resultat["categorie"] == "brelan"
    # les 3 du brelan puis kickers decroissants
    valeurs = [c.valeur() for c in resultat["chosen5"]]
    assert valeurs == [12, 12, 12, 14, 9]


def test_brelan_bas():
    main = [
        Carte("2", "pique"),
        Carte("2", "coeur"),
        Carte("2", "carreau"),
        Carte("A", "trefle"),
        Carte("K", "pique"),
    ]
    resultat = evaluer_main(main)
    assert resultat["categorie"] == "brelan"
    valeurs = [c.valeur() for c in resultat["chosen5"]]
    assert valeurs == [2, 2, 2, 14, 13]


# --- tests pour suite (straight) ---

def test_suite_basique():
    main = [
        Carte("5", "pique"),
        Carte("6", "coeur"),
        Carte("7", "carreau"),
        Carte("8", "trefle"),
        Carte("9", "pique"),
    ]
    resultat = evaluer_main(main)
    assert resultat["categorie"] == "suite"


def test_suite_chosen5():
    main = [
        Carte("5", "pique"),
        Carte("6", "coeur"),
        Carte("7", "carreau"),
        Carte("8", "trefle"),
        Carte("9", "pique"),
    ]
    resultat = evaluer_main(main)
    # triees de la plus haute a la plus basse
    valeurs = [c.valeur() for c in resultat["chosen5"]]
    assert valeurs == [9, 8, 7, 6, 5]


def test_suite_ace_high():
    main = [
        Carte("10", "pique"),
        Carte("J", "coeur"),
        Carte("Q", "carreau"),
        Carte("K", "trefle"),
        Carte("A", "pique"),
    ]
    resultat = evaluer_main(main)
    assert resultat["categorie"] == "suite"
    valeurs = [c.valeur() for c in resultat["chosen5"]]
    assert valeurs == [14, 13, 12, 11, 10]


def test_suite_ace_low_wheel():
    main = [
        Carte("A", "pique"),
        Carte("2", "coeur"),
        Carte("3", "carreau"),
        Carte("4", "trefle"),
        Carte("5", "pique"),
    ]
    resultat = evaluer_main(main)
    assert resultat["categorie"] == "suite"
    # wheel : 5-high, l'as est en bas
    valeurs = [c.valeur() for c in resultat["chosen5"]]
    assert valeurs == [5, 4, 3, 2, 14]


def test_pas_de_wrap_around():
    # Q-K-A-2-3 n'est PAS une suite
    main = [
        Carte("Q", "pique"),
        Carte("K", "coeur"),
        Carte("A", "carreau"),
        Carte("2", "trefle"),
        Carte("3", "pique"),
    ]
    resultat = evaluer_main(main)
    assert resultat["categorie"] != "suite"


# --- tests pour couleur (flush) ---

def test_flush_basique():
    main = [
        Carte("A", "coeur"),
        Carte("J", "coeur"),
        Carte("9", "coeur"),
        Carte("6", "coeur"),
        Carte("3", "coeur"),
    ]
    resultat = evaluer_main(main)
    assert resultat["categorie"] == "couleur"


def test_flush_chosen5():
    main = [
        Carte("K", "pique"),
        Carte("10", "pique"),
        Carte("8", "pique"),
        Carte("5", "pique"),
        Carte("2", "pique"),
    ]
    resultat = evaluer_main(main)
    assert resultat["categorie"] == "couleur"
    # rangs decroissants
    valeurs = [c.valeur() for c in resultat["chosen5"]]
    assert valeurs == [13, 10, 8, 5, 2]


def test_flush_pas_si_couleurs_differentes():
    main = [
        Carte("A", "coeur"),
        Carte("J", "coeur"),
        Carte("9", "coeur"),
        Carte("6", "pique"),
        Carte("3", "coeur"),
    ]
    resultat = evaluer_main(main)
    assert resultat["categorie"] != "couleur"


# --- tests pour full house ---

def test_full_house_basique():
    main = [
        Carte("K", "pique"),
        Carte("K", "coeur"),
        Carte("K", "carreau"),
        Carte("3", "trefle"),
        Carte("3", "pique"),
    ]
    resultat = evaluer_main(main)
    assert resultat["categorie"] == "full"


def test_full_house_chosen5():
    main = [
        Carte("10", "pique"),
        Carte("10", "coeur"),
        Carte("10", "carreau"),
        Carte("A", "trefle"),
        Carte("A", "pique"),
    ]
    resultat = evaluer_main(main)
    assert resultat["categorie"] == "full"
    # brelan d'abord, puis la paire
    valeurs = [c.valeur() for c in resultat["chosen5"]]
    assert valeurs == [10, 10, 10, 14, 14]


# --- tests pour carre (four of a kind) ---

def test_carre_basique():
    main = [
        Carte("7", "pique"),
        Carte("7", "coeur"),
        Carte("7", "carreau"),
        Carte("7", "trefle"),
        Carte("A", "pique"),
    ]
    resultat = evaluer_main(main)
    assert resultat["categorie"] == "carre"


def test_carre_chosen5():
    main = [
        Carte("J", "pique"),
        Carte("J", "coeur"),
        Carte("J", "carreau"),
        Carte("J", "trefle"),
        Carte("K", "pique"),
    ]
    resultat = evaluer_main(main)
    assert resultat["categorie"] == "carre"
    # les 4 du carre puis le kicker
    valeurs = [c.valeur() for c in resultat["chosen5"]]
    assert valeurs == [11, 11, 11, 11, 13]


# --- tests pour quinte flush (straight flush) ---

def test_quinte_flush_basique():
    main = [
        Carte("5", "coeur"),
        Carte("6", "coeur"),
        Carte("7", "coeur"),
        Carte("8", "coeur"),
        Carte("9", "coeur"),
    ]
    resultat = evaluer_main(main)
    assert resultat["categorie"] == "quinte flush"


def test_quinte_flush_chosen5():
    main = [
        Carte("5", "coeur"),
        Carte("6", "coeur"),
        Carte("7", "coeur"),
        Carte("8", "coeur"),
        Carte("9", "coeur"),
    ]
    resultat = evaluer_main(main)
    valeurs = [c.valeur() for c in resultat["chosen5"]]
    assert valeurs == [9, 8, 7, 6, 5]


def test_quinte_flush_royale():
    main = [
        Carte("10", "pique"),
        Carte("J", "pique"),
        Carte("Q", "pique"),
        Carte("K", "pique"),
        Carte("A", "pique"),
    ]
    resultat = evaluer_main(main)
    assert resultat["categorie"] == "quinte flush"
    valeurs = [c.valeur() for c in resultat["chosen5"]]
    assert valeurs == [14, 13, 12, 11, 10]


def test_quinte_flush_ace_low():
    main = [
        Carte("A", "carreau"),
        Carte("2", "carreau"),
        Carte("3", "carreau"),
        Carte("4", "carreau"),
        Carte("5", "carreau"),
    ]
    resultat = evaluer_main(main)
    assert resultat["categorie"] == "quinte flush"
    valeurs = [c.valeur() for c in resultat["chosen5"]]
    assert valeurs == [5, 4, 3, 2, 14]
