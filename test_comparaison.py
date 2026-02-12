# tests pour la selection meilleure main et comparaison entre joueurs
from carte import Carte
from evaluateur import evaluer_main, meilleure_main, comparer_joueurs


# --- tests pour meilleure main 5 parmi 7 ---

def test_meilleure_main_choisit_la_paire():
    board = [
        Carte("A", "pique"),
        Carte("2", "carreau"),
        Carte("3", "coeur"),
        Carte("4", "trefle"),
        Carte("9", "carreau"),
    ]
    hole = [Carte("5", "pique"), Carte("K", "carreau")]
    resultat = meilleure_main(board, hole)
    # la meilleure main est une suite (A-2-3-4-5)
    assert resultat["categorie"] == "suite"


def test_meilleure_main_flush_avec_6_coeurs():
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
    # doit choisir les 5 meilleurs coeurs : A, J, 9, 6, 4
    valeurs = [c.valeur() for c in resultat["chosen5"]]
    assert valeurs == [14, 11, 9, 6, 4]


def test_meilleure_main_board_plays():
    # le board est une suite, les cartes du joueur n'aident pas
    board = [
        Carte("5", "pique"),
        Carte("6", "carreau"),
        Carte("7", "coeur"),
        Carte("8", "trefle"),
        Carte("9", "carreau"),
    ]
    hole = [Carte("2", "pique"), Carte("3", "carreau")]
    resultat = meilleure_main(board, hole)
    assert resultat["categorie"] == "suite"
    valeurs = [c.valeur() for c in resultat["chosen5"]]
    assert valeurs == [9, 8, 7, 6, 5]


# --- tests pour comparaison entre joueurs ---

def test_comparer_paire_vs_carte_haute():
    board = [
        Carte("2", "pique"),
        Carte("5", "carreau"),
        Carte("8", "coeur"),
        Carte("J", "trefle"),
        Carte("K", "carreau"),
    ]
    joueurs = {
        "joueur1": [Carte("K", "pique"), Carte("3", "carreau")],
        "joueur2": [Carte("A", "pique"), Carte("9", "carreau")],
    }
    resultat = comparer_joueurs(board, joueurs)
    # joueur1 a une paire de K, joueur2 a juste carte haute
    assert resultat["gagnants"] == ["joueur1"]


def test_comparer_egalite_split():
    board = [
        Carte("5", "pique"),
        Carte("6", "carreau"),
        Carte("7", "coeur"),
        Carte("8", "trefle"),
        Carte("9", "carreau"),
    ]
    joueurs = {
        "joueur1": [Carte("A", "pique"), Carte("A", "carreau")],
        "joueur2": [Carte("K", "pique"), Carte("Q", "carreau")],
    }
    resultat = comparer_joueurs(board, joueurs)
    # les deux ont la meme suite 5-9, c'est un split
    assert sorted(resultat["gagnants"]) == ["joueur1", "joueur2"]


def test_comparer_carre_kicker():
    board = [
        Carte("7", "pique"),
        Carte("7", "carreau"),
        Carte("7", "coeur"),
        Carte("7", "trefle"),
        Carte("2", "carreau"),
    ]
    joueurs = {
        "joueur1": [Carte("A", "pique"), Carte("K", "pique")],
        "joueur2": [Carte("Q", "pique"), Carte("J", "pique")],
    }
    resultat = comparer_joueurs(board, joueurs)
    # joueur1 gagne avec kicker A
    assert resultat["gagnants"] == ["joueur1"]
