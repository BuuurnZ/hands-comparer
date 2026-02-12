# tests pour la classe Carte
from carte import Carte


def test_creer_carte():
    c = Carte("A", "pique")
    assert c.rang == "A"
    assert c.couleur == "pique"


def test_creer_carte_numerique():
    c = Carte("10", "coeur")
    assert c.rang == "10"
    assert c.couleur == "coeur"


def test_valeur_carte_numerique():
    c = Carte("2", "carreau")
    assert c.valeur() == 2


def test_valeur_carte_figure():
    assert Carte("J", "pique").valeur() == 11
    assert Carte("Q", "coeur").valeur() == 12
    assert Carte("K", "carreau").valeur() == 13
    assert Carte("A", "trefle").valeur() == 14


def test_valeur_carte_10():
    c = Carte("10", "pique")
    assert c.valeur() == 10


def test_egalite_cartes():
    c1 = Carte("A", "pique")
    c2 = Carte("A", "pique")
    assert c1 == c2


def test_cartes_differentes():
    c1 = Carte("A", "pique")
    c2 = Carte("K", "pique")
    assert c1 != c2


def test_representation_carte():
    c = Carte("A", "pique")
    assert str(c) == "A de pique"
