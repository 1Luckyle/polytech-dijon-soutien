import random

# Red, Green, Blue, Yellow, Purple, White
COLORS = ["R", "G", "B", "Y", "P", "W"]
LENGTH = 4
NB_TRY = 12

def random_code():
    code = []
    for i in range(LENGTH):
        code.append(random.choice(COLORS))
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