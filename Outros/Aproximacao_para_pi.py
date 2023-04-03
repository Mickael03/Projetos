from random import random, randrange
from math import cos, sin, pi, sqrt
import matplotlib.pyplot as plt

#Construção do circulo
def circulo(x = 0, y = 0, raio = 1):
    a = [x + raio*cos(pi*ang/180) for ang in range(361)]
    b = [y + raio*sin(pi*ang/180) for ang in range(361)]
    return a,b

#Construção dos quadrado
def quadrado(x = 0,y = 0, raio = 1):
    
    a = (x - raio, y - raio)
    b = (x + raio, y - raio)
    c = (x + raio, y + raio)
    d = (x - raio, y + raio)
    
    return [a[0],b[0],c[0],d[0],a[0]], [a[1],b[1],c[1],d[1],a[1]]  

#n pontos aleatórios
def pontos(x = 0, y = 0, raio = 1, n = 10):
    
    a = [x + (-1)**randrange(1,3)*raio*random() for i in range(n)]
    b = [y + (-1)**randrange(1,3)*raio*random() for i in range(n)]
    
    return a, b

def valor_pi(x = 0, y = 0, raio = 1,  n = 10, grafico = False):
    
    #Funções de construção
    a, b = pontos(x = x, y = y, raio = raio, n = n)
    if grafico == True:
        c, d = circulo(x = x, y = y, raio = raio)
        e, f = quadrado(x = x,y = y, raio = raio)
    
    #Gráfico
    if grafico == True:
        plt.plot(a, b, linestyle = ' ', color = 'r', marker = '.') #Pontos aleatórios
        plt.plot(c, d, color = 'g') #Círculo
        plt.plot(e,f) #Quadrado
    
    #Contagem dos pontos internos ao círculo
    count = 0
    for i in range(len(a)):
        d = (x - a[i])**2 + (y - b[i])**2
        if sqrt(d) <= raio:
            count += 1
    
    print(f"valor aproximado de pi: {4*(count/len(a))}")