#Lista de Exercícios

def exercicio2():

    largura = int(input("digite a largura: "))
    altura = int(input("digite a altura: "))

    for i in range(altura):
        if i == 0 or i == altura - 1:
            for j in range(largura):
                print("#",end = "")
            print("")
        else:
            print("#", end = "")
            for k in range(largura - 2):
                print(" ", end = "")
            print("#")

#Lista adicional de exercí­cios
def n_primos(n, elementos = False):
    
    lista = []
    if n <= 1:
        return 0
    else:
        i = 1
        while i <= n:
            count = 0
            for j in range(1,n+1):
                rest = i % j
                if rest == 0:
                    count += 1
            if count == 2:
                lista.append(i)
            i += 1
    
    if elementos == True:
        return lista
    else:
        return len(lista)

def soma_quadrados(hip = 1):
    
    cat1 = hip - 1
    cat2 = hip - 1
    lista = []
    
    i = 1
    while i <= cat1:
        j = 1
        while j <= cat2:
            soma = i**2 + j**2
            if soma == hip**2:
                lista.append((i,j))
            j += 1
        i += 1
    
    if len(lista) == 0:
        return None
 
    return lista[0]
        
def soma_hipotenusas(n):
    
    lista = []
    
    i = 1
    while i <= n:
        if soma_quadrados(i) != None:
            lista.append(i)
        i += 1
    
    count = 0
    for i in lista:
        count += i
        
    return count
