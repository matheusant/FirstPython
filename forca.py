def play():
    print("*******************")
    print("Jogo de Forca")
    print("*******************")

    secret_word = "banana"
    hit = False
    hanged = False
    total_attempts = 5

    print(f"A palavra tem {len(secret_word)} letras\n")
    hint = ""

    for i in range(len(secret_word)):
        hint += "_"

    while not hit and not hanged:
        print(f"\ntotal de tentativas {total_attempts}\n")
        print(hint)
        attempt = input("Digite uma letra ")
        attempt = attempt.strip()

        index = 0

        for letter in secret_word:
            if attempt.lower() == letter.lower():
                x = list(hint)
                x[index] = letter.upper()
                hint = "".join(x)

            index += 1

        if attempt not in secret_word:
            total_attempts -= 1
        if hint.lower() == secret_word.lower():
            print(f"Você acertou a palavra {secret_word.upper()}!")
            hit = True
        if total_attempts == 0:
            print(f"Você perdeu!!! A palavra era {secret_word.upper()}")
            hanged = True

    print("Fim de jogo")


if __name__ == "__main__":
    play()
