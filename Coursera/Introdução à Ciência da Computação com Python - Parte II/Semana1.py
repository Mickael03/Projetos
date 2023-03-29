def cria_matriz(n_linhas,n_colunas, valor = None):
       
    matriz = []
    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            if valor != None:
                elemento = valor
            else:
                elemento = int(input(f"Entre com elemento [{str(i)}][{str(j)}]: "))
            linha.append(elemento)
        matriz.append(linha)
    
    return matriz

def le_matriz(n__linha = None, n_colunas = None):
    
    n_linhas = int(input("Numero de linhas: "))
    n_colunas = int(input("Número de colunas: "))
    matriz = cria_matriz(n_linhas, n_colunas)
    
    return matriz

def dimensoes(matriz):
    
    linhas = str(len(matriz))
    colunas = str(len(matriz[0]))
    
    return print(linhas + "X" + colunas)

def soma_matrizes(m1,m2):

    dimensao1 = dimensoes(m1)
    dimensao2 = dimensoes(m2)
    
    if dimensao1 != dimensao2:
        return False
    
    soma = []
    for i in range(len(m1)):
        linha = []
        for j in range(len(m1[0])):
            linha.append(m1[i][j] + m2[i][j])
        soma.append(linha)
        
    return soma

def imprime_matriz(matriz):
    
    for i in matriz:
        for j in range(len(i)):
            if j < len(i) - 1:
                print(i[j], end = " ")
            else:
                print(i[j])

def sao_multiplicaveis(m1,m2):
    
    if len(m1[0]) != len(m2):
        return False
    else:
        return True