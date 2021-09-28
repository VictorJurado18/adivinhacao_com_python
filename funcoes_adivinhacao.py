def seleciona_nivel(nivel):
    if(nivel == 1):
        #facil
        total_de_tentativas = 20
    elif(nivel == 2):
        #medio
        total_de_tentativas = 10
    elif(nivel == 3):
        #dificil
        total_de_tentativas = 5
    
    return total_de_tentativas

def verifica_chute(chute, numero_secreto,total_tentativas):
    if(chute == numero_secreto):
        print("\033[0;32;47mVocê acertou!!!\033[m")
        print("Fim do jogo...")
        total_tentativas = 0
        return total_tentativas   
    else:
        if(chute > numero_secreto):
            print("\033[0;31;40mVocê errou! O seu chute foi maior do que o número secreto.\033[m")
            total_tentativas -=1
            return total_tentativas
            
        elif(chute < numero_secreto):
            print("\033[0;31;40mVocê errou! O seu chute foi menor do que o número secreto.\033[m")
            total_tentativas -=1
            return total_tentativas
        