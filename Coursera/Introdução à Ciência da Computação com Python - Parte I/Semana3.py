import math

#Lista de Exerci�cio
def exercicio1():
    
    n = int(input("Digiter um n�mero inteiro: "))
    
    return "Par" if n%2 == 0 else "�mpar"
    
def exercicio2():
    
    n = int(input("Digiter um n�mero inteiro: "))
    
    return "Fizz" if n%3 == 0 else n

def exercicio3():
    
    n = int(input("Digiter um n�mero inteiro: "))
    
    return "Buzz" if n%5 == 0 else n

def exercicio4():
    
    n = int(input("Digiter um n�mero inteiro: "))
    return "FizzBuzz" if(n%3 == 0 and n%5 == 0) else n

def exercicio5():
    
    n1 = float(input("Entre com primeiro n��mero: "))
    n2 = float(input("Entre com segundo n��mero: "))
    n3 = float(input("Entre com terceiro n��mero: "))
    
    if n1 <= n2:
        if n2 <= n3:
            return "crescente"
        else:
            return "n��o est�� em ordem crescente"
    else:
        return "n��o est�� em ordem crescente"

#Lista adicional
def exercicio1_ad():
    
    x1 = float(input("Coordenada x do ponto A: "))
    y1 = float(input("Coordenada y do ponto A: "))
    x2 = float(input("Coordenada x do ponto B: "))
    y2 = float(input("Coordenada y do ponto B: "))
    
    distancia = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    
    return "longe" if distancia > 10 else "perto"

def exercicio2_ad():
    
    a = float(input("Valor do coeficiente A: "))
    b = float(input("Valor do coeficiente B: "))
    c = float(input("Valor do coeficiente C: "))
    
    delta = b**2 - 4*a*c
    
    if delta < 0:
        return "esta equa����o n��o possui ra�zes reais"
    elif delta == 0:
        x = -b/(2*a)
        return f"a raiz desta equa����o � {x}"
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        if x1 < x2:
            return f"as ra��zes da equa�㍋o s��o {x1} e {x2}"
        return f"as ra��zes da equa��o s��o {x2} e {x1}"