import math
import re

#Palavras
def lista_palavras(texto):
    
    #Transformar o texto em um lista com as palavras
    palavras = texto.lower().split()
    
    #Sinais a serem eliminados
    sinais = [".",",","!","?",";",":"]
    
    #Eliminação de sinais nas palavras
    for i in range(len(palavras)):
        for j in sinais:
            palavras[i] = palavras[i].replace(j,'')
        
    return palavras

def quantidade_palavras(texto):

    #dicionario vazio
    quantidade = {}
    
    #Lista de palavras
    palavras = lista_palavras(texto)
    
    #Contagem de palavras
    for i in range(len(palavras)):
        quantidade[palavras[i]] = palavras.count(palavras[i])
        
    #Conclusão
    return quantidade

def Tamanho_medio_palavras(texto):
    
    dicionario = quantidade_palavras(texto)
    
    numero_palavras = 0
    for i in dicionario:
        numero_palavras += dicionario[i]
    
    tamanho = 0
    for i in dicionario:
        tamanho += len(i)*dicionario[i]
        
    return tamanho/numero_palavras

def relacao_typertoken(texto):
    
    dicionario = quantidade_palavras(texto)
    
    palavras_distintas = len(dicionario)
    
    numero_palavras = 0
    for i in dicionario:
        numero_palavras += dicionario[i]
    
    return palavras_distintas/numero_palavras

def razao_hapaxlegomana(texto):
    
    palavras = quantidade_palavras(texto)
    
    #Palavras que aparecem um unica vez
    count1 = 0
    for i in palavras:
        if palavras[i] == 1:
            count1 += 1
    
    #Total de palavras
    count2 = 0
    for i in palavras:
        count2 += palavras[i]
    
    return count1/count2

#Sentenças
def separa_sentencas(texto):
    
    #Separa as sentenças
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]

    return sentencas

def numero_sentencas(texto):
    return len(separa_sentencas(texto))

def tamanho_medio_sentencas(texto):
    
    sentencas = separa_sentencas(texto)
    
    for i in range(len(sentencas)):
        sentencas[i] = sentencas[i].rstrip()
        
    #Número de caracteres
    count = 0
    for i in sentencas:
        count += len(i)
        
    return count/len(sentencas)

#Frases
def separa_frases(texto):
    
    #Separa as sentenças
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    
    #Separando as frases
    frases = []
    for i in sentencas:
        for j in re.split(r'[,:;]+', i):
            frases.append(j)
        
    return frases

def numero_frases(texto):
    return len(separa_frases(texto))

def tamanho_medio_frases(texto):
    
    frases = separa_frases(texto)
    
    for i in range(len(frases)):
        frases[i] = frases[i].rstrip()
        
    #Número de caracteres
    count = 0
    for i in frases:
        count += len(i)
        
    return count/len(frases)

#Calculo
def complexidade(texto):
    return numero_frases(texto)/numero_sentencas(texto)

def compara_assinatura(as_a, as_b):
    
    soma = 0
    for i in range(len(as_a)):
        soma += math.fabs(as_a[i]-as_b[i])
        
    return soma/6

def calcula_assinatura(texto):
    
    wal = Tamanho_medio_palavras(texto)
    ttr = relacao_typertoken(texto)
    hlr = razao_hapaxlegomana(texto)
    sal = tamanho_medio_sentencas (texto)
    sac = complexidade(texto)
    pal = tamanho_medio_frases(texto)

    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    
    #Pontuação dos texto
    pontos = []
    for i in textos:
        pontos.append(compara_assinatura(calcula_assinatura(i),ass_cp))
    
    #Seleção do menor valor
    count = pontos[0]
    valor = 0
    for i in range(len(pontos)):
        if pontos[i] < count:
            count = pontos[i]
            valor = i
            
    return valor + 1