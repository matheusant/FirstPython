import random

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

secret_number = random.randrange(1, 101)
##print(secret_number)
total_attempts = 0
round_attempt = 1

print("Qual o nivel de dificuldade?")
print("1 - Fácil\n2 - Médio\n3 - Difícil")

level = int(input("Defina o nível da dificuldade: "))

if level == 1:
    total_attempts = 100
elif level == 2:
    total_attempts = 20
elif level == 3:
    total_attempts = 5

for round_attempt in range(1, total_attempts + 1):
    print("Tentativa {} de {}".format(round_attempt, total_attempts))
    attempt = int(input("Digite um número entre 1 e 100: "))

    if attempt < 1 or attempt > 100:
        if round_attempt == total_attempts:
            print("Você errou! O número fica entre 1 e 100")
        else:
            print("Número inválido, digite um número entre 1 e 100")
        continue
    more = attempt > secret_number
    less = attempt < secret_number
    if round_attempt == total_attempts:
        print("Você perdeu! O número secreto era {}".format(secret_number))
        break
    elif more:
        print("Você errou! O número digitado é maior que o secreto")
    elif less:
        print("Você errou! O número digitado é menor que o secreto")
    elif attempt == secret_number:
        print("Você acertou")
        break

print("Fim de jogo")
