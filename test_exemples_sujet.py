# tests des exemples donnes dans le sujet de l'examen
from carte import Carte
from evaluateur import meilleure_main, comparer_joueurs


# Exemple A - suite ace-low (wheel)
def test_exemple_a_wheel():
    board = [
        Carte("A", "trefle"),
        Carte("2", "carreau"),
        Carte("3", "coeur"),
        Carte("4", "pique"),
        Carte("9", "carreau"),
    ]
    hole = [Carte("5", "trefle"), Carte("K", "carreau")]
    resultat = meilleure_main(board, hole)
    assert resultat["categorie"] == "suite"
    valeurs = [c.valeur() for c in resultat["chosen5"]]
    assert valeurs == [5, 4, 3, 2, 14]


# Exemple B - suite ace-high
def test_exemple_b_ace_high_straight():
    board = [
        Carte("10", "trefle"),
        Carte("J", "carreau"),
        Carte("Q", "coeur"),
        Carte("K", "pique"),
        Carte("2", "carreau"),
    ]
    hole = [Carte("A", "trefle"), Carte("3", "carreau")]
    resultat = meilleure_main(board, hole)
    assert resultat["categorie"] == "suite"
    valeurs = [c.valeur() for c in resultat["chosen5"]]
    assert valeurs == [14, 13, 12, 11, 10]


# Exemple C - flush avec plus de 5 cartes de meme couleur
def test_exemple_c_flush_meilleurs_5():
    board = [
        Carte("A", "coeur"),
        Carte("J", "coeur"),
        Carte("9", "coeur"),
        Carte("4", "coeur"),
        Carte("2", "trefle"),
    ]
    hole = [Carte("6", "coeur"), Carte("K", "carreau")]
    resultat = meilleure_main(board, hole)
    assert resultat["categorie"] == "couleur"
    valeurs = [c.valeur() for c in resultat["chosen5"]]
    assert valeurs == [14, 11, 9, 6, 4]


# Exemple D - board plays (egalite)
def test_exemple_d_board_plays_egalite():
    board = [
        Carte("5", "trefle"),
        Carte("6", "carreau"),
        Carte("7", "coeur"),
        Carte("8", "pique"),
        Carte("9", "carreau"),
    ]
    joueurs = {
        "joueur1": [Carte("A", "trefle"), Carte("A", "carreau")],
        "joueur2": [Carte("K", "trefle"), Carte("Q", "carreau")],
    }
    resultat = comparer_joueurs(board, joueurs)
    # les deux ont la meme suite, c'est un split
    assert sorted(resultat["gagnants"]) == ["joueur1", "joueur2"]
    # les deux doivent avoir categorie suite
    assert resultat["resultats"]["joueur1"]["categorie"] == "suite"
    assert resultat["resultats"]["joueur2"]["categorie"] == "suite"


# Exemple E - carre sur le board, kicker decide
def test_exemple_e_carre_kicker():
    board = [
        Carte("7", "trefle"),
        Carte("7", "carreau"),
        Carte("7", "coeur"),
        Carte("7", "pique"),
        Carte("2", "carreau"),
    ]
    joueurs = {
        "joueur1": [Carte("A", "trefle"), Carte("K", "trefle")],
        "joueur2": [Carte("Q", "trefle"), Carte("J", "trefle")],
    }
    resultat = comparer_joueurs(board, joueurs)
    assert resultat["gagnants"] == ["joueur1"]
    assert resultat["resultats"]["joueur1"]["categorie"] == "carre"
    assert resultat["resultats"]["joueur2"]["categorie"] == "carre"
