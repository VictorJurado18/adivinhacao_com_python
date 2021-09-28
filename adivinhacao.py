import random
import funcoes_adivinhacao

print("\033[0;32;40m#####################################")
print("#  Bem vindo ao jogo de Adivinhação #")
print("#####################################\033[m\n")

numero_secreto = random.randrange(1,101)

print("Qual nível de dificuldade?")
print("\033[0;32;40m(1) Fácil \033[0;33;40m(2) Médio \033[0;31;40m(3) Difícil\033[m")

nivel = int(input("Defina o nível: "))

total_tentativas = funcoes_adivinhacao.seleciona_nivel(nivel)


while total_tentativas > 0:
    print(f"Você ainda tem {total_tentativas} tentativa(as).")
    chute = int(input("Digite um número entre 1 e 100: "))
    total_tentativas = funcoes_adivinhacao.verifica_chute(chute, numero_secreto, total_tentativas)
    
    

