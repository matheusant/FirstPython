import random


def play():
    presentation()
    secret_word = get_secret_word()

    errors = 0
    hit = False
    hanged = False

    print(f"A palavra tem {len(secret_word)} letras\n")
    hint = ["_" for letter in secret_word]

    while not hit and not hanged:
        print(hint, '\n')
        attempt = input("Digite uma letra ")
        attempt = attempt.strip().upper()

        if attempt in secret_word:
            right_attempt(attempt, hint, secret_word)
        else:
            errors += 1
            draw_hang(errors)

        hit = "_" not in hint
        hanged = errors == 7

    if hit:
        print("Você acertou a palavra {}".format(secret_word))
    else:
        print("Você perdeu a palavra era {}".format(secret_word))


def right_attempt(attempt, hint, secret_word):
    index = 0
    for letter in secret_word:
        if attempt == letter:
            hint[index] = letter
        index += 1


def get_secret_word():
    words = list()
    with open("palavras.txt", "r") as file:
        for word in file:
            word = word.strip()
            words.append(word)
    rand_index = random.randrange(0, len(words))
    secret_word = words[rand_index].upper()
    return secret_word


def presentation():
    print("*******************")
    print("Jogo de Forca")
    print("*******************")


def draw_hang(errors):
    print("  _______     ")
    print(" |/      |    ")

    if errors == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if errors == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if errors == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if errors == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if errors == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if errors == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if errors == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    play()
