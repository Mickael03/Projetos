#Lista de exercícios
def remove_repetidos(lista):
    
    lista2 = []
    for i in lista:
        if i not in lista2:
            lista2.append(i)
            
    return sorted(lista2)

def soma_elementos(lista):
    
    count = 0
    for i in lista:
        count += i
    
    return count

#Lista adicional de exercícios

def maior_elemento (lista):
    
    elemento = lista[0]
    for i in lista:
        if i > elemento:
            elemento = i
    
    return elemento

def exercicio2():
    
    fim = False
    lista = []
    while fim != True:
        i = int(input("Digite um número: "))
        if i != 0:
            lista.append(i)
        else:
            fim = True
    
    for i in range(1,len(lista)+1):
        print(lista[-i])