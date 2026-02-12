# tests pour verifier que l'ordre de priorite entre categories est respecte
from carte import Carte
from evaluateur import evaluer_main, score_main


def test_paire_bat_carte_haute():
    paire = [Carte("2", "pique"), Carte("2", "coeur"), Carte("5", "carreau"), Carte("7", "trefle"), Carte("9", "pique")]
    haute = [Carte("A", "pique"), Carte("K", "coeur"), Carte("Q", "carreau"), Carte("J", "trefle"), Carte("8", "pique")]
    assert score_main(evaluer_main(paire)) > score_main(evaluer_main(haute))


def test_double_paire_bat_paire():
    dp = [Carte("3", "pique"), Carte("3", "coeur"), Carte("2", "carreau"), Carte("2", "trefle"), Carte("5", "pique")]
    paire = [Carte("A", "pique"), Carte("A", "coeur"), Carte("K", "carreau"), Carte("Q", "trefle"), Carte("J", "pique")]
    assert score_main(evaluer_main(dp)) > score_main(evaluer_main(paire))


def test_brelan_bat_double_paire():
    brelan = [Carte("2", "pique"), Carte("2", "coeur"), Carte("2", "carreau"), Carte("5", "trefle"), Carte("7", "pique")]
    dp = [Carte("A", "pique"), Carte("A", "coeur"), Carte("K", "carreau"), Carte("K", "trefle"), Carte("Q", "pique")]
    assert score_main(evaluer_main(brelan)) > score_main(evaluer_main(dp))


def test_suite_bat_brelan():
    suite = [Carte("5", "pique"), Carte("6", "coeur"), Carte("7", "carreau"), Carte("8", "trefle"), Carte("9", "pique")]
    brelan = [Carte("A", "pique"), Carte("A", "coeur"), Carte("A", "carreau"), Carte("K", "trefle"), Carte("Q", "pique")]
    assert score_main(evaluer_main(suite)) > score_main(evaluer_main(brelan))


def test_couleur_bat_suite():
    couleur = [Carte("2", "coeur"), Carte("5", "coeur"), Carte("7", "coeur"), Carte("9", "coeur"), Carte("J", "coeur")]
    suite = [Carte("10", "pique"), Carte("J", "coeur"), Carte("Q", "carreau"), Carte("K", "trefle"), Carte("A", "pique")]
    assert score_main(evaluer_main(couleur)) > score_main(evaluer_main(suite))


def test_full_bat_couleur():
    full = [Carte("2", "pique"), Carte("2", "coeur"), Carte("2", "carreau"), Carte("3", "trefle"), Carte("3", "pique")]
    couleur = [Carte("A", "coeur"), Carte("K", "coeur"), Carte("Q", "coeur"), Carte("J", "coeur"), Carte("9", "coeur")]
    assert score_main(evaluer_main(full)) > score_main(evaluer_main(couleur))


def test_carre_bat_full():
    carre = [Carte("2", "pique"), Carte("2", "coeur"), Carte("2", "carreau"), Carte("2", "trefle"), Carte("3", "pique")]
    full = [Carte("A", "pique"), Carte("A", "coeur"), Carte("A", "carreau"), Carte("K", "trefle"), Carte("K", "pique")]
    assert score_main(evaluer_main(carre)) > score_main(evaluer_main(full))


def test_quinte_flush_bat_carre():
    qf = [Carte("5", "coeur"), Carte("6", "coeur"), Carte("7", "coeur"), Carte("8", "coeur"), Carte("9", "coeur")]
    carre = [Carte("A", "pique"), Carte("A", "coeur"), Carte("A", "carreau"), Carte("A", "trefle"), Carte("K", "pique")]
    assert score_main(evaluer_main(qf)) > score_main(evaluer_main(carre))
