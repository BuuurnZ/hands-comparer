# tests pour les regles de tie-break entre mains de meme categorie
from carte import Carte
from evaluateur import evaluer_main, score_main, meilleure_main, comparer_joueurs


# --- tie-break carte haute ---

def test_tiebreak_carte_haute_premiere_carte():
    main1 = [Carte("A", "pique"), Carte("10", "coeur"), Carte("8", "carreau"), Carte("5", "trefle"), Carte("3", "pique")]
    main2 = [Carte("K", "pique"), Carte("10", "carreau"), Carte("8", "trefle"), Carte("5", "coeur"), Carte("3", "carreau")]
    s1 = score_main(evaluer_main(main1))
    s2 = score_main(evaluer_main(main2))
    assert s1 > s2


def test_tiebreak_carte_haute_deuxieme_carte():
    main1 = [Carte("A", "pique"), Carte("K", "coeur"), Carte("8", "carreau"), Carte("5", "trefle"), Carte("3", "pique")]
    main2 = [Carte("A", "carreau"), Carte("Q", "carreau"), Carte("8", "trefle"), Carte("5", "coeur"), Carte("3", "carreau")]
    s1 = score_main(evaluer_main(main1))
    s2 = score_main(evaluer_main(main2))
    assert s1 > s2


def test_tiebreak_carte_haute_egalite():
    main1 = [Carte("A", "pique"), Carte("K", "coeur"), Carte("8", "carreau"), Carte("5", "trefle"), Carte("3", "pique")]
    main2 = [Carte("A", "carreau"), Carte("K", "carreau"), Carte("8", "trefle"), Carte("5", "coeur"), Carte("3", "carreau")]
    s1 = score_main(evaluer_main(main1))
    s2 = score_main(evaluer_main(main2))
    assert s1 == s2


# --- tie-break paire ---

def test_tiebreak_paire_rang_paire():
    main1 = [Carte("A", "pique"), Carte("A", "coeur"), Carte("8", "carreau"), Carte("5", "trefle"), Carte("3", "pique")]
    main2 = [Carte("K", "pique"), Carte("K", "coeur"), Carte("8", "trefle"), Carte("5", "coeur"), Carte("3", "carreau")]
    s1 = score_main(evaluer_main(main1))
    s2 = score_main(evaluer_main(main2))
    assert s1 > s2


def test_tiebreak_paire_kicker():
    main1 = [Carte("10", "pique"), Carte("10", "coeur"), Carte("A", "carreau"), Carte("5", "trefle"), Carte("3", "pique")]
    main2 = [Carte("10", "carreau"), Carte("10", "trefle"), Carte("K", "trefle"), Carte("5", "coeur"), Carte("3", "carreau")]
    s1 = score_main(evaluer_main(main1))
    s2 = score_main(evaluer_main(main2))
    assert s1 > s2


# --- tie-break double paire ---

def test_tiebreak_double_paire_haute():
    main1 = [Carte("A", "pique"), Carte("A", "coeur"), Carte("3", "carreau"), Carte("3", "trefle"), Carte("5", "pique")]
    main2 = [Carte("K", "pique"), Carte("K", "coeur"), Carte("3", "pique"), Carte("3", "coeur"), Carte("5", "carreau")]
    s1 = score_main(evaluer_main(main1))
    s2 = score_main(evaluer_main(main2))
    assert s1 > s2


def test_tiebreak_double_paire_basse():
    main1 = [Carte("A", "pique"), Carte("A", "coeur"), Carte("5", "carreau"), Carte("5", "trefle"), Carte("3", "pique")]
    main2 = [Carte("A", "carreau"), Carte("A", "trefle"), Carte("4", "pique"), Carte("4", "coeur"), Carte("3", "carreau")]
    s1 = score_main(evaluer_main(main1))
    s2 = score_main(evaluer_main(main2))
    assert s1 > s2


def test_tiebreak_double_paire_kicker():
    main1 = [Carte("A", "pique"), Carte("A", "coeur"), Carte("K", "carreau"), Carte("K", "trefle"), Carte("Q", "pique")]
    main2 = [Carte("A", "carreau"), Carte("A", "trefle"), Carte("K", "pique"), Carte("K", "coeur"), Carte("J", "carreau")]
    s1 = score_main(evaluer_main(main1))
    s2 = score_main(evaluer_main(main2))
    assert s1 > s2


# --- tie-break brelan ---

def test_tiebreak_brelan_rang():
    main1 = [Carte("K", "pique"), Carte("K", "coeur"), Carte("K", "carreau"), Carte("5", "trefle"), Carte("3", "pique")]
    main2 = [Carte("Q", "pique"), Carte("Q", "coeur"), Carte("Q", "carreau"), Carte("5", "coeur"), Carte("3", "carreau")]
    s1 = score_main(evaluer_main(main1))
    s2 = score_main(evaluer_main(main2))
    assert s1 > s2


def test_tiebreak_brelan_kicker():
    main1 = [Carte("7", "pique"), Carte("7", "coeur"), Carte("7", "carreau"), Carte("A", "trefle"), Carte("3", "pique")]
    main2 = [Carte("7", "trefle"), Carte("7", "pique"), Carte("7", "coeur"), Carte("K", "trefle"), Carte("3", "carreau")]
    s1 = score_main(evaluer_main(main1))
    s2 = score_main(evaluer_main(main2))
    assert s1 > s2


# --- tie-break suite ---

def test_tiebreak_suite_carte_haute():
    main1 = [Carte("6", "pique"), Carte("7", "coeur"), Carte("8", "carreau"), Carte("9", "trefle"), Carte("10", "pique")]
    main2 = [Carte("5", "pique"), Carte("6", "coeur"), Carte("7", "carreau"), Carte("8", "trefle"), Carte("9", "carreau")]
    s1 = score_main(evaluer_main(main1))
    s2 = score_main(evaluer_main(main2))
    assert s1 > s2


def test_tiebreak_suite_wheel_plus_basse():
    # wheel (5-high) perd contre suite 6-high
    main1 = [Carte("2", "pique"), Carte("3", "coeur"), Carte("4", "carreau"), Carte("5", "trefle"), Carte("6", "pique")]
    main2 = [Carte("A", "pique"), Carte("2", "coeur"), Carte("3", "carreau"), Carte("4", "trefle"), Carte("5", "carreau")]
    s1 = score_main(evaluer_main(main1))
    s2 = score_main(evaluer_main(main2))
    assert s1 > s2


# --- tie-break couleur ---

def test_tiebreak_flush_carte_haute():
    main1 = [Carte("A", "coeur"), Carte("J", "coeur"), Carte("9", "coeur"), Carte("6", "coeur"), Carte("3", "coeur")]
    main2 = [Carte("K", "pique"), Carte("J", "pique"), Carte("9", "pique"), Carte("6", "pique"), Carte("3", "pique")]
    s1 = score_main(evaluer_main(main1))
    s2 = score_main(evaluer_main(main2))
    assert s1 > s2


def test_tiebreak_flush_deuxieme_carte():
    main1 = [Carte("A", "coeur"), Carte("Q", "coeur"), Carte("9", "coeur"), Carte("6", "coeur"), Carte("3", "coeur")]
    main2 = [Carte("A", "pique"), Carte("J", "pique"), Carte("9", "pique"), Carte("6", "pique"), Carte("3", "pique")]
    s1 = score_main(evaluer_main(main1))
    s2 = score_main(evaluer_main(main2))
    assert s1 > s2


# --- tie-break full ---

def test_tiebreak_full_brelan():
    main1 = [Carte("K", "pique"), Carte("K", "coeur"), Carte("K", "carreau"), Carte("3", "trefle"), Carte("3", "pique")]
    main2 = [Carte("Q", "pique"), Carte("Q", "coeur"), Carte("Q", "carreau"), Carte("A", "trefle"), Carte("A", "pique")]
    s1 = score_main(evaluer_main(main1))
    s2 = score_main(evaluer_main(main2))
    assert s1 > s2


def test_tiebreak_full_paire():
    main1 = [Carte("K", "pique"), Carte("K", "coeur"), Carte("K", "carreau"), Carte("A", "trefle"), Carte("A", "pique")]
    main2 = [Carte("K", "trefle"), Carte("K", "pique"), Carte("K", "coeur"), Carte("Q", "trefle"), Carte("Q", "pique")]
    s1 = score_main(evaluer_main(main1))
    s2 = score_main(evaluer_main(main2))
    assert s1 > s2


# --- tie-break carre ---

def test_tiebreak_carre_rang():
    main1 = [Carte("A", "pique"), Carte("A", "coeur"), Carte("A", "carreau"), Carte("A", "trefle"), Carte("3", "pique")]
    main2 = [Carte("K", "pique"), Carte("K", "coeur"), Carte("K", "carreau"), Carte("K", "trefle"), Carte("3", "carreau")]
    s1 = score_main(evaluer_main(main1))
    s2 = score_main(evaluer_main(main2))
    assert s1 > s2


def test_tiebreak_carre_kicker():
    main1 = [Carte("7", "pique"), Carte("7", "coeur"), Carte("7", "carreau"), Carte("7", "trefle"), Carte("A", "pique")]
    main2 = [Carte("7", "trefle"), Carte("7", "pique"), Carte("7", "coeur"), Carte("7", "carreau"), Carte("K", "pique")]
    s1 = score_main(evaluer_main(main1))
    s2 = score_main(evaluer_main(main2))
    assert s1 > s2


# --- tie-break quinte flush ---

def test_tiebreak_quinte_flush_carte_haute():
    main1 = [Carte("6", "coeur"), Carte("7", "coeur"), Carte("8", "coeur"), Carte("9", "coeur"), Carte("10", "coeur")]
    main2 = [Carte("5", "pique"), Carte("6", "pique"), Carte("7", "pique"), Carte("8", "pique"), Carte("9", "pique")]
    s1 = score_main(evaluer_main(main1))
    s2 = score_main(evaluer_main(main2))
    assert s1 > s2
