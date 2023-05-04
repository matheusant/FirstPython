import random


def play():
    print("*******************")
    print("Jogo de Forca")
    print("*******************")

    words = list()
    with open("palavras.txt", "r") as file:
        for word in file:
            word = word.strip()
            words.append(word)

    rand_index = random.randrange(0, len(words))

    secret_word = words[rand_index].upper()
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
            index = 0
            for letter in secret_word:
                if attempt == letter:
                    hint[index] = letter
                index += 1
        else:
            errors += 1

        hit = "_" not in hint
        hanged = errors == 6

    if hit:
        print("Você acertou a palavra {}".format(secret_word))
    else:
        print("Você perdeu a palavra era {}".format(secret_word))
    print("Fim de jogo")


if __name__ == "__main__":
    play()
