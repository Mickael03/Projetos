def menor_nome(lista_nomes):
    
    #Lista de nomes sem os espaços
    nomes = [i.strip() for i in lista_nomes]
    
    #Determinar o menor nome
    tamanho = len(nomes[0])
    count = 0
    for i in range(len(nomes)):
        if len(nomes[i]) == tamanho:
            count += 1
        elif len(nomes[i]) < tamanho:
            tamanho = len(nomes[i])
            count = 1
    
    #Lista com os nomes ordenados por tamanho
    lista = [i.capitalize() for i in nomes if len(i) == tamanho]
    
    return lista[0] #Primeiro da lista ordenarda

def primeiro_lex(lista):
    
    #Transforma os nomes em um número
    valor = []
    for i in lista:
        count = 0
        pontuacao = []
        for j in i:
            count += ord(j)
            pontuacao.append(count)
        valor.append((pontuacao,i))
        
    #Ordena os valores numero dos nomes
    valor.sort()
    
    #Lista os nomes em ordem
    nomes = [valor[i][1] for i in range(len(valor))]
    
    return nomes[0] #Retorna somente o primeiro nome da lista

def maiusculas(frase):
    
    elementos = ""
    for i in frase:
        if ord(i) in range(65,91):
            elementos += i
        
    return elementos

def conta_letras(frase, contar="vogais"):
    
    vogais = [65,69,73,79,85] #Vogais minusculas em ascII
    frase = frase.upper() ##Transformando o string em ascii minusculo
    frase = frase.replace(" ","")
    count = 0 #Contagem de caracteres
    
    if contar == "vogais":
        for i in frase:
            if ord(i) in vogais:
                count += 1
        return count
    elif contar == "consoantes":
        vogais = vogais + [" "]
        for i in frase:
            if ord(i) not in vogais:
                count += 1
        return count
