#Lista de Exerci­cio
def maximo(n,m):
    
    return n if n > m else m

def maior_primo(n):
    
    while 2 < n:
        i = 1
        count = 0
        while i < n:
            res = n%i
            if res == 0:
                count += 1
            i += 1
        if count == 1:
            return n
        n -= 1
        
    return 2

def vogal(n):
    
    lista = ["a","e","i","o","u"] #lista de vogais
    
    i = 0
    while i < len(lista):
        if n.lower() in lista[i]:
            return True
        i += 1
        
    return False
        
#Lista adicional
def fizzbuzz(n):
    
    if n%3 == 0 and n%5 != 0:
        return "Fizz"
    elif n%3 != 0 and n%5 == 0:
        return "Buzz"
    elif n%3 == 0 and n%5 == 0:
        return "FizzBuzz"
    else:
        return n

def maximo_ad(x, y, z):
    
    if x >= y:
        if x >= z:
            return x
        else:
            return z
    elif x < y:
        if y > z:
            return y
        else:
            return z
