print("*******************")
print("Jogo de Adivinhação")
print("*******************")

##### Digitando números até acertar ######
# secret_number = 42
#
# while True:
#     attempt = int(input("Digite um número: "))
#     more = attempt > secret_number
#     less = attempt < secret_number
#     if more:
#         print("Você errou! O número digitado é maior que o secreto")
#     elif less:
#         print("Você errou! O número digitado é menor que o secreto")
#     elif attempt == secret_number:
#         break
#     # try:
#     #     attempt = int(input("Digite outro numero: "))
#     # except:
#     #     print("Formato inválido")
#     #     attempt = int(input("Digite um número inteiro: "))
# print("Você acertou")
# print("Fim de jogo")


##### Digitando números até o total de tentivas acabar ######

secret_number = 42
total_attempts = 5
round_attempt = 1

while round_attempt <= total_attempts:
    print("Tentativa {} de {}".format(round_attempt, total_attempts))
    attempt = int(input("Digite um número: "))
    more = attempt > secret_number
    less = attempt < secret_number
    if more:
        print("Você errou! O número digitado é maior que o secreto")
    elif less:
        print("Você errou! O número digitado é menor que o secreto")
    elif attempt == secret_number:
        print("Você acertou")
        break

    round_attempt = round_attempt + 1
print("Fim de jogo")
