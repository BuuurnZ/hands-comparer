# classe pour representer une carte de poker


VALEURS_FIGURES = {
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}


class Carte:
    def __init__(self, rang, couleur):
        self.rang = rang
        self.couleur = couleur

    def valeur(self):
        if self.rang in VALEURS_FIGURES:
            return VALEURS_FIGURES[self.rang]
        return int(self.rang)

    def __eq__(self, autre):
        return self.rang == autre.rang and self.couleur == autre.couleur

    def __repr__(self):
        return f"{self.rang} de {self.couleur}"

    def __str__(self):
        return f"{self.rang} de {self.couleur}"

    def __hash__(self):
        return hash((self.rang, self.couleur))
