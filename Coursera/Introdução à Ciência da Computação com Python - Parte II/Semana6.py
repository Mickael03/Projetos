#Funções das aulas
def busca_binaria(lista,elemento):
    
    inicio = 0
    final = len(lista)
    
    meio = (inicio + final)//2
    print(meio, lista, lista[meio])
    
    if lista[meio] > elemento:
        return busca_binaria(lista[:meio], elemento)
    elif lista[meio] < elemento:
        return busca_binaria(lista[meio+1:], elemento)
    else:
        return meio

def sort(lista, i = 0):
    return [[i] for i in lista]

def merge(lista):
    
    for i in range(len(lista)-1,2):
        print(i)
        if lista[i] > lista[i + 1]:
            lista[i] = lista[i + 1]
    
    return lista

def MergeSort(lista):
    
    elementos = sort(lista)
    return elementos


#Primeira lista de Exercícios
def soma_lista(lista):
    
    final = len(lista) - 1
    soma = lista[final]
    
    if final == 0:
        return soma
    
    return soma_lista(lista[:final]) + soma

def encontra_impares(lista, impares = []):
    
    if len(lista) == 0:
        return impares
    elif lista[0] % 2 != 0:
        impares.append(lista[0])
   
    return encontra_impares(lista[1:], impares = impares)

def incomodam(n):
    
    if n > 0:
        return "incomodam" + " " + incomodam(n-1)
    else:
        return ""

def elefantes(n, i = 1, res = False):
    
    if i == 1:
        return "Um elefante incomada muita gente" + elefantes(n, i + 1, res = True)
    elif i < n:
        if res == True:
            return "\n" + str(i) + " elefantes " + incomodam(i) +"muito mais" + elefantes(n, i, res = False)
        elif res == False:
            return "\n" + str(i) + " elefantes incomodam muita gente" + elefantes(n, i + 1, res = True)
    else:
        return "\n" + str(i) + " elefantes " + incomodam(n) + "muito mais"
    
#Segunda lista de Exercícios
def fibonacci(n):
    
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n - 2)

def fatorial(n):
    
    if n == 1 or n == 0:
        return 1
    else:
        return n*fatorial(n-1)
    
k = sort([1,7,30,4,5,6,0,7,89,8])
r = merge(k[:])