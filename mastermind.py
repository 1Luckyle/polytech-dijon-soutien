import random

# PARAMETRES :
# Il suffit d'ajouter une lettre associé à une couleur sous le formant "LETTRE": "Nom_de_la_couleur"
COLORS = {
    "R": "Red",
    "G": "Green",
    "B": "Blue",
    "Y": "Yellow",
    "P": "Purple",
    "W": "White",
}
LENGTH = 4  # nombre d'éléments dans le code secret
NB_TRY = 12  # nombre maximal de tentatives pour la résolution du code secret


def random_code():
    code = []
    # Ici on crée la liste des lettres pour le code secret, liste associé aux couleurs disponibles définies dans COLORS
    lettres = list(COLORS)
    for i in range(LENGTH):
        code.append(random.choice(lettres))
    return code

def verif_essai(essai, code_secret):
    correct = 0
    partiel = 0
    # copies pour ne pas compter deux fois la même couleur
    reste_essai = list(essai)
    reste_secret = list(code_secret)

    # vérifie les bonnes couleurs au bon emplacement
    for i in range(LENGTH):
        if reste_essai[i] == reste_secret[i]:
            correct = correct + 1
            reste_essai[i] = None
            reste_secret[i] = None

    # vérifie les bonnes couleurs au mauvais emplacement
    for couleur in reste_essai:
        if couleur is not None and couleur in reste_secret:
            partiel = partiel + 1
            reste_secret[reste_secret.index(couleur)] = None
    
    return correct, partiel

def input_essai():
    while True:
        saisie = input("Votre code : ").strip().upper()
        if len(saisie) == LENGTH and all(c in COLORS for c in saisie):
            return list(saisie)
        print(f"Saisie invalide, entrez {LENGTH} lettres parmi {', '.join(COLORS)}.")

def game():
    print("Couleurs disponibles :", ", ".join(COLORS))
    code_secret = random_code()

    for essai_numero in range(1, NB_TRY + 1):
        essai = input_essai()
        correct, partiel = verif_essai(essai, code_secret)
        print(f"Correct : {correct} | Partiel : {partiel}")
        if correct == LENGTH:
            score = NB_TRY - essai_numero
            print(f"Bravo, code trouvé en {essai_numero} essais ! Score : {score}")
            return
    print(f"Perdu ! Le code secret était : {''.join(code_secret)}")

if __name__ == "__main__":
    game()