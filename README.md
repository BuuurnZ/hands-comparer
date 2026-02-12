# hands-comparer

Comparateur de mains de Texas Hold'em Poker en Python.

## Description

Programme qui evalue et compare des mains de poker Texas Hold'em.
Pour chaque joueur, on determine la meilleure main de 5 cartes parmi les 7 disponibles (2 cartes privees + 5 cartes communes).

## Lancer les tests

```bash
pip install -r requirements.txt
pytest -v
```

## Regles

- On suit les regles standard du Texas Hold'em (voir https://en.wikipedia.org/wiki/List_of_poker_hands)
- Les couleurs ne servent qu'a detecter les flush, pas de tie-break par couleur
- L'as peut etre haut (A-K-Q-J-10) ou bas (A-2-3-4-5) dans une suite
- Pas de wrap-around (Q-K-A-2-3 est invalide)

## Ordre du chosen5

- **Straight / Straight Flush** : de la plus haute a la plus basse (wheel = 5,4,3,2,A)
- **Four of a Kind** : les 4 cartes du carre puis le kicker
- **Full House** : les 3 du brelan puis les 2 de la paire
- **Flush / High Card** : rangs decroissants
- **Three of a Kind** : les 3 du brelan puis kickers decroissants
- **Two Pair** : paire haute, paire basse, kicker
- **One Pair** : les 2 de la paire puis kickers decroissants

## Validation des entrees

On suppose qu'il n'y a pas de cartes dupliquees dans l'entree. Pas de validation explicite.