import forca
import adivinhacao

print("*******************")
print("Seja bem vindo")
print("*******************")

print("Jogos disponiveis:\n1 - Forca\n2 - Adivinhação")
game = int(input("Escolha o jogo: "))

if game == 1:
    print("Entrando no jogo da forca")
    forca.play()
elif game == 2:
    print("Entrando no jogo de adivinhação")
    adivinhacao.play()
else:
    print("Jogo inválido")
