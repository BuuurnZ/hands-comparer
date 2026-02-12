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


# --- tests chosen5 est bien un sous-ensemble des 7 cartes ---

def test_chosen5_sous_ensemble_des_7():
    board = [
        Carte("A", "trefle"),
        Carte("2", "carreau"),
        Carte("3", "coeur"),
        Carte("4", "pique"),
        Carte("9", "carreau"),
    ]
    hole = [Carte("5", "trefle"), Carte("K", "carreau")]
    toutes = board + hole
    resultat = meilleure_main(board, hole)
    # chaque carte du chosen5 doit etre dans les 7 cartes
    for c in resultat["chosen5"]:
        assert c in toutes


def test_chosen5_exactement_5_cartes():
    board = [
        Carte("A", "coeur"),
        Carte("J", "coeur"),
        Carte("9", "coeur"),
        Carte("4", "coeur"),
        Carte("2", "trefle"),
    ]
    hole = [Carte("6", "coeur"), Carte("K", "carreau")]
    resultat = meilleure_main(board, hole)
    assert len(resultat["chosen5"]) == 5


def test_chosen5_cartes_distinctes():
    board = [
        Carte("K", "pique"),
        Carte("K", "coeur"),
        Carte("K", "carreau"),
        Carte("3", "trefle"),
        Carte("3", "pique"),
    ]
    hole = [Carte("A", "pique"), Carte("7", "carreau")]
    resultat = meilleure_main(board, hole)
    # pas de doublons dans chosen5
    chosen = resultat["chosen5"]
    for i in range(len(chosen)):
        for j in range(i + 1, len(chosen)):
            assert chosen[i] != chosen[j] or chosen[i].couleur != chosen[j].couleur


# --- tests tie-break multi-joueurs avec 7 cartes ---

def test_tiebreak_paire_kicker_via_joueurs():
    board = [
        Carte("10", "pique"),
        Carte("10", "coeur"),
        Carte("5", "carreau"),
        Carte("3", "trefle"),
        Carte("2", "pique"),
    ]
    joueurs = {
        "joueur1": [Carte("A", "pique"), Carte("7", "carreau")],
        "joueur2": [Carte("K", "pique"), Carte("8", "carreau")],
    }
    resultat = comparer_joueurs(board, joueurs)
    # les deux ont paire de 10, joueur1 gagne avec kicker A
    assert resultat["gagnants"] == ["joueur1"]


def test_tiebreak_flush_via_joueurs():
    board = [
        Carte("2", "coeur"),
        Carte("5", "coeur"),
        Carte("8", "coeur"),
        Carte("J", "coeur"),
        Carte("3", "pique"),
    ]
    joueurs = {
        "joueur1": [Carte("A", "coeur"), Carte("4", "carreau")],
        "joueur2": [Carte("K", "coeur"), Carte("4", "pique")],
    }
    resultat = comparer_joueurs(board, joueurs)
    # les deux ont flush coeur, joueur1 a l'as
    assert resultat["gagnants"] == ["joueur1"]


def test_tiebreak_full_via_joueurs():
    board = [
        Carte("7", "pique"),
        Carte("7", "coeur"),
        Carte("7", "carreau"),
        Carte("5", "trefle"),
        Carte("2", "pique"),
    ]
    joueurs = {
        "joueur1": [Carte("A", "pique"), Carte("A", "coeur")],
        "joueur2": [Carte("K", "pique"), Carte("K", "coeur")],
    }
    resultat = comparer_joueurs(board, joueurs)
    # les deux ont full (7-7-7 + paire), joueur1 a paire d'as
    assert resultat["gagnants"] == ["joueur1"]
