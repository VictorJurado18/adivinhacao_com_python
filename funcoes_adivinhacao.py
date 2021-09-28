def bem_vindo():
    print("\033[0;32;40m#####################################")
    print("#  Bem vindo ao jogo de Adivinhação #")
    print("#####################################\033[m\n")

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

def verifica_chute(chute, numero_secreto, total_tentativas):
    if(chute == numero_secreto):
        print("\033[1;32;40mVocê acertou!!!\033[m")
        total_tentativas = 0
        ganhou = True
        return [total_tentativas, ganhou]  

    else:
        if(chute > numero_secreto):
            print("\033[1;31;40mVocê errou! O seu chute foi maior do que o número secreto.\033[m")
            total_tentativas = total_tentativas - 1
            ganhou = False
            return [total_tentativas, ganhou]  
            
        elif(chute < numero_secreto):
            print("\033[1;31;40mVocê errou! O seu chute foi menor do que o número secreto.\033[m")
            total_tentativas = total_tentativas - 1
            ganhou = False
            return [total_tentativas, ganhou]  
        
def verifica_se_ganhou(ganhou, numero_secreto):
    if ganhou == True:
        print("\033[1;32;40mParabéns, você ganhou!\033[m")
    else:
        print(f"\033[1;31;40mQue pena, você não conseguiu adivinhar o numero secreto\nO numero secreto era {numero_secreto}\033[m")