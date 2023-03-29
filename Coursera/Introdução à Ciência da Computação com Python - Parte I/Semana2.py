def perimentro():
    x = float(input("Digite o valor correspondente ao lado de um quadrado: "))
    return print(f"perímetro: {4*x} - área: {x**2}")

def notas(notas = 4):
    
    soma = 0
    for i in range(1,notas + 1):
        nota = float(input(f"Entre com a nota {i}: "))
        soma += nota
    
    return print(f"A média aritmética é {soma/notas}")

def exercicio1():
    
    nome = input("Digite o nome do cliente: ")
    dia = input("Digite o dia de vencimento: ")
    mes = input("Digite o mês de vencimento: ")
    valor = input("Digite o valor da fatura: ")
    
    return print(f"\n\nOlá, {nome}\nA sua fatura com vencimento em {dia} de {mes} no valor de R$ {valor} está fechada.")

def exercicio2():
    
    segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
    
    dias = segundos//86400
    horas = (segundos%86400)//3600
    minutos = ((segundos%86400)%3600)//60
    segundos = (((segundos%86400)%3600)%60)
    
    return print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos.")

def exercicio3():
    
    numero = int(input("Digite um número inteiro: "))
    
    dezena = (numero//10)%10
    
    return print(f"O dígito das dezenas é {dezena}")