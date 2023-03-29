import random

def ordenada(lista):
    
   x = ordena(lista[:])
   
   for i in range(len(lista)):
       if lista[i] != x[i]:
           return False
   return True

def busca(lista,elemento):
    
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return False

def lista_grande(n):
    #Função somete sorteia números ate um milhão
    lista = [random.randrange(1000000000) for i in range(n)]
    return lista

def ordena(lista):
    
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[j] < lista[i]:
                lista[i],lista[j] = lista[j], lista[i]

    return lista