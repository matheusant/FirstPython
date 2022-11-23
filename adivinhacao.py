print("*******************")
print("Jogo de Adivinhação")
print("*******************")

secret_number = 42
attempt = int(input("Digite um número: "))

while attempt != secret_number:
    bigger = attempt > secret_number
    lesser = attempt < secret_number
    if bigger:
        print("Você errou! O número digitado é maior que o secreto")
    elif lesser:
        print("Você errou! O número digitado é menor que o secreto")
    try:
        attempt = int(input("Digite outro numero: "))
    except:
        print("Formato inválido")
        attempt = int(input("Digite um número inteiro: "))
print("Você acertou")
print("Fim de jogo")
