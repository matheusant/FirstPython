def play():
    print("*******************")
    print("Jogo de Forca")
    print("*******************")

    secret_word = "banana"
    hit = False
    hanged = False

    print(f"A palavra tem {len(secret_word)} letras\n")
    hint = ""

    for i in range(len(secret_word)):
        hint += "_"

    print(hint)
    while not hit and not hanged:
        attempt = input("Digite uma letra ")
        attempt = attempt.strip()

        index = 1
        for letter in secret_word:
            if attempt.lower() == letter.lower():
                print(f'A letra chutada foi {attempt.upper()} e ela está na posição {index}')
            index += 1
    print("Fim de jogo")


if __name__ == "__main__":
    play()
