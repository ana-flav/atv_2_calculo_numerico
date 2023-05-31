import pandas as pd
from rich import print

#TODO: PLOTAR A DISTANCIA, VERIFICAR COM PROFESSOR

def criando_tabela_caso1(valores):
    print("\n\n\n")
    print("[red]* * :warning: TABELA DE ITERAÇÕES :warning: * *[/red] \n")
    nome_cols = ['K', 'X1', 'X2', 'E']
    tabela = pd.DataFrame(valores, columns=nome_cols)
    tabela_final = tabela.set_index('K')
    print(tabela_final)

def caso_sistema_2():
    lista_adicionar_valores = []
    e = float('inf')

    print("\n\n[red]--------- Equação primeira ------[/red] \n ")
    a11 = float(input("Digite a11: "))
    a12 = float(input("Digite a12: "))
    b1 = float(input("Digite o b1: "))

    print("\n\n[red]--------- Equação segunda ------[/red] \n ")
    a21 = float(input("Digite a21: "))
    a22 = float(input("Digite a22: "))
    b2 = float(input("Digite o b2: "))

    
    x1 = lambda x2: 1 / a11 * (b1 - a12 * x2)
    x2 = lambda x1: 1 / a22 * (b2 - a21 * x1)

    print("\n\n[red]---- Iteração incial. -----[/red]")
    valor_x1 = int(input("Digite o valor inicial de x1: "))
    valor_x2 = int(input("Digite o valor inicial de x2: "))

    print("\n\n[red]--- Tolerancia e maximo de interações[/red] ")
    n = int(input("Digite o n da tolerância assim E<10^-n :  "))
    M=int(input("Digite o maximo de interações: "))
    tolerancia = 10**(-n)

    print("\n\n[red]Insira os valores exatos[/red]")
    a = int(input("Digite o primeiro valor exato: "))
    b = int(input("Digite o segundo valor exato: "))

    k=0
    lista_adicionar_valores.append([0, 0, 0, float('inf')])
    while k<M or e>tolerancia:

        resultado_x1 = float(x1(valor_x2))
        resultado_x2 = float(x2(valor_x1))
        k += 1
        if k%2 == 0:
            e = abs(valor_x1-resultado_x1)
        else:
            e = abs(valor_x2-resultado_x2)
        
        lista_adicionar_valores.append([k, resultado_x1, resultado_x2, e])
        valor_x1=resultado_x1
        valor_x2=resultado_x2

    print("\n\n\n")
    print(f":fireworks: [green]A solução aproximada é [{valor_x1}, {valor_x2}] [/green]")
    print("\n")
    print(":fireworks: [blue]A distância entre a solução exata e aproximada é: [/blue]")
    criando_tabela_caso1(lista_adicionar_valores)



caso_sistema_2()


    
    
    

   




