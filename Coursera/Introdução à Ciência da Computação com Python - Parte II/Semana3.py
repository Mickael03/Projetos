class Triangulo:
    
    def __init__(self,lado1,lado2,lado3):
        self.a = lado1
        self.b = lado2
        self.c = lado3
    
    def a(self):
        return self.a
    
    def b(self):
        return self.b
    
    def c(self):
        return self.c
        
    def perimetro(self):
        return self.a + self.b + self.c
    
    def tipo_lado(self):
        
        if self.a == self.b == self.c: #Triângulo equiláterio
            return "equilátero"
        elif (self.a != self.b) and (self.a != self.c):#escaleno
            return "escaleno"
        else:
            return "isósceles"
        
    def retangulo(self):
        
        lista = [self.a,self.b,self.c]
        lista.sort()
        
        #Teste para triângulo retangulo
        if lista[0]**2 + lista[1]**2 == lista[2]**2:
            return True
        else:
            return False
    
    def semelhantes(self,triangulo):
             
        #Ordenação dos triângulo
        lista1 = [self.a,self.b,self.c]
        lista1.sort()
        
        #Ordenação do triângulo recebido
        lista2 = [triangulo.a,triangulo.b,triangulo.c]
        lista2.sort()
    
        #Teste de semelhaça
        #Caso os lados do primeiro triangulo sejam maiores
        r = lista1[0]/lista2[0]
        count = 0
        for i in range(len(lista1)):
            if r == lista1[i]/lista2[i]:
                count += 1
        if count == 3:
            return True
        else:
            return False
            
def soma_matriz(m1,m2):

    soma = []
    for i in range(len(m1)):
        linha = []
        for j in range(len(m1[0])):
            linha.append(m1[i][j] + m2[i][j])
        soma.append(linha)
        
    return soma

def multiplicacao_matriz(m1,m2):
    
    if len(m1[0]) != len(m2):
        return print("Matrizes não multiplicaveis")
    
    c = []
    for i in range(len(m1)): #Número de linhas
        c.append([])
        for j in range(len(m2[0])): #Número de colunas
            c[i].append(0)
            for k in range(len(m1[0])):
                c[i][j] += m1[i][k]*m2[k][j]
    return c