#Lista de ExerciÂ­cio
def exercicio1():
    
    n = int(input("Digite o valor de n: "))
    
    if n < 0 or type(n) != int:
        return "Fatorial não definido"
    elif n == 0 or n == 1:
        return 1
    else:
        i = 2
        count = 1
        while i <= n:
            count = count*i
            i += 1
        return count

def exercicio2():
    
    n = int(input("Digite o valor de n: "))
    
    i = 0
    while i < n:
        j = 2*i + 1
        print(j)
        i += 1

def exercicio3():
    
    numero = int(input("Digite um número inteiro: "))
    count = 0
    
    while numero != 0:
        
        count += numero%10
        numero = numero//10
    
    return count

#Lista adicional
def exercicio1_ad():
    
    numero = int(input("Digite um número inteiro: "))
    
    i = 1
    count = 0
    while i <= int(numero):
        
        if numero % i == 0:
            count += 1
            
        if count > 2:
            return "não primo"
        
        i += 1
    
    return "primo"

def exercicio2_ad():
    
    numero = int(input("Digite um número inteiro: "))
    valor = False
    
    while numero//10 != 0:
        
        n1 = numero%10
        numero = numero//10
        n2 = numero%10
        
        if n1 == n2:
            valor = True
    
    if valor:
        return "Sim"
    else:
        return "Não"