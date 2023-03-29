def busca(lista,elemento): 
        
    inicio = 0
    final = len(lista) - 1
    
    while inicio <= final:
        
        meio = (inicio + final)//2
        
        print(meio)
        
        if lista[meio] == elemento:
            return meio
        else:
            if lista[meio] < elemento:
                inicio = meio + 1
            else:
                final = meio - 1
        
    return False

def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                print(lista)
    return lista

def insertion_sort(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            for j in range(i):
                if lista[j] > lista[i + 1]:
                    lista[j], lista[i + 1] = lista[i + 1], lista[j]
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            print(lista)
    return lista