#Adiconar a opção para jogadores humanos

def dois():
    
    valor = True
    
    while valor:
        
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        
        if n >= m:
            valor = False
        else:
            valor = True
            print("\nOops! quantidade de peças inválida! Tente de novo.")
            print("n deve se menor que m\n")
    
    count1 = 0
    count2 = 0
    
    while n > 0:
        print("\n*** Jogador - 01 ***\n")
        n = n - usuario_escolhe_jogada(n, m)
        if n <= 0:
            count1 += 1
        print("\n*** Jogador - 02 ***\n")
        n = n - usuario_escolhe_jogada(n, m)
        if n <= 0:
            count2 += 1
    
    if count1 > count2:
        print("Vitória do Jogador - 01")
    else:
        print("Vitória de Jogador - 02")

def computador_escolhe_jogada(n,m):#Função para um jogador
    
    if n % (m + 1) == 0:
        retirada = m
        print(f"\nO computador tirou {retirada} peça.")
        print(f"Agora restam {n-retirada} peças no tabuleiro.\n")
        return retirada
    else:
        retirada = n % (m + 1)
        print(f"\nO computador tirou {retirada} peça.")
        print(f"Agora restam {n-retirada} peças no tabuleiro.\n")
        return retirada
    
def usuario_escolhe_jogada(n,m):#Função para um jogador
    
    if n <= 0:
        return 0
    
    valor = True
    
    while valor:
        
        retiradas = int(input("Quantas peças você vai tirar? "))
        
        if n < retiradas:
            print("\nOops! Jogada inválida! Tente de novo.\n")
        elif m < retiradas:
            print("\nOops! Jogada inválida! Tente de novo.\n")
        elif retiradas <= 0:
            print("\nOops! Jogada inválida! Tente de novo.\n")
        else:
            valor = False

    print(f"Agora restam {n - retiradas} peças no tabuleiro.\n")
    
    return retiradas

def partida():#Partida contra computador
    
    valor = True
    
    while valor:
        
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        
        if n >= m:
            valor = False
        else:
            valor = True
            print("\nOops! quantidade de peças inválida! Tente de novo.")
            print("n deve se menor que m\n")
            
    if n == m:
        print("\nComputador Começar!\n")
        n = n - computador_escolhe_jogada(n, m)
        print("\nFim de jogo! O computador ganhou!")
    elif n % (m + 1) == 0:
        print("\nVocê começar!\n")
        while n > 0:
            n = n - usuario_escolhe_jogada(n, m)
            n = n - computador_escolhe_jogada(n, m)
        print("\nFim do jogo! O computador ganhou!")
    else:
        print("\nComputador Começar!\n")
        while n > 0:
            n = n - computador_escolhe_jogada(n, m)
            n = n - usuario_escolhe_jogada(n,m)
        print("\nFim do jogo! O computador ganhou!")


def selecao():#Seleção do tipo de partida
    
    print("Bem-vindo ao jogo do NIM! Escolha:\n\n")
    print("1 - para jogar uma partida isolada (Vs Computador)")
    print("2 - para jogar um campeonato (Três Rodadas)")
    print("3 - para dois jogadores")
    
    selecao = int(input("\nOpção: "))
    valor = True
    
    
    if selecao not in [1,2,3]:
        
        while valor:
            
            print("\n\nOops! Opção inválida! Tente de novo.\n")
            print("1 - para jogar uma partida isolada")
            print("2 - para jogar um campeonato")
            print("3 - para dois jogadores")
            selecao = int(input("\nOpção: "))
            
            if selecao == 1 or selecao == 2:
                valor = False
    
    if selecao == 1:
        print("\nVocê escolheu uma partida isolada!\n")
        partida()
    elif selecao == 2:
        print("\nVoce escolheu um campeonato!\n")
        for i in range(1,4):
            print(f"\n**** Rodada {i} ****\n")
            partida()
        
        print("**** Final do campeonato! ****")
        print(f"\nPlacar: Você {0} X {3} Computador\n")
    else:
        print("\nPartida de dois jogadores\n")
        dois()

selecao()