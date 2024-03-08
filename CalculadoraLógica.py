# Importação de Bibliotecas
import pandas as pd
import os
from tabulate import tabulate

# Tabelas com valores predefinidos de possíveis operações com 1 ou 2 variáveis
Col1 = pd.DataFrame({'A': [1, 0]})
Col2 = pd.DataFrame({'A': [1, 1, 0, 0],
                     'B': [0, 1, 1, 0]})

# Função principal, onde ocorre toda a interação com o usúario e funcionamento da Calculadora.
def Menu():
    while True:

        try:
            print("Calculadora Lógica!\nEscolha a opção desejada:\n\n1- Calculadora Disjunção V\n2- Calculadora Conjunção ∧\n3- Calculadora Condicional →\n4- Calculadora Bicondicional ↔\n5- Calculadora Negação ¬\n6- Gerador de Tabela Verdade\n7- Encerrar calculadora\n")
            opcao = int(input("Digite a Opção Desejada: "))

            if 1 <= opcao <= 6:
                os.system("cls")
                conectivo(opcao)
                input("\nPrecione enter para continuar e retornar ao menu principal ")
                os.system("cls")
            elif opcao == 7:
                print("Fim da execução\nTenha um bom dia!")
                break
            else:
                input("Escolha uma opção válida!\nPrecione enter para continuar ")
                os.system("cls")
        except ValueError: # Se for inserido algo diferente de um número
            input("Informe apenas valores numéricos...\nPrecione enter para continuar ")
            os.system("cls")

# Função para Verificação da seleção do meu e chamar as funções da calculadora
def conectivo(opcao):
    match opcao:
        
        case 1:
            CalculadoraDisjuncao()
        case 2:
            CalculadoraConjuncao()
        case 3:
            CalculadoraCondicional()
        case 4:
            CalculadoraBicondicional()
        case 5:
            CalculadoraNegacao()
        case 6:
            while True:

                try:
                    print("Escolha uma tabela verdade das seguintes lógicas\n1- Disjunção V\n2- Conjunção ∧\n3- Condicional →\n4- Bicondicional ↔\n5- Negação ¬\n")
                    opcaoTabela = int(input("Digite a Tabela Desejada: "))

                    if 1 <= opcaoTabela <= 5:
                        os.system("cls")
                        if opcaoTabela == 1:
                            print("Tabela Verdade Disjunção\n")
                            CriaTabela("V", 2)
                            break
                        elif opcaoTabela == 2:
                            print("Tabela Verdade Conjunção\n")
                            CriaTabela("∧", 2)
                            break
                        elif opcaoTabela == 3:
                            print("Tabela Verdade Condicional\n")
                            CriaTabela("⭢", 2)
                            break
                        elif opcaoTabela == 4:
                            print("Tabela Verdade Bicondicional\n")
                            CriaTabela("↔", 2)
                            break
                        elif opcaoTabela == 5:
                            print("Tabela Verdade Negação\n")
                            CriaTabela("¬", 1)
                            break
                        
                    else:
                        input("Escolha uma opção válida!\nPrecione enter para continuar ")
                        os.system("cls")
                except ValueError: # Se for inserido algo diferente de um número
                    input("Informe apenas valores numéricos...\nPrecione enter para continuar ")
                    os.system("cls")
                    
# Função para Calcular Operação de Disjunção
def CalculadoraDisjuncao():
    Colunas = pd.DataFrame({'A': [], 'B': []}) 
    valorA = []
    valorB = []
    i = 0
    while i < 4 : 
        try:
            A = int(input(f"Insira um valor entre 0 e 1 para o {i+1}° A: "))
            B = int(input(f"Insira um valor entre 0 e 1 para o {i+1}° B: "))
            i = i + 1
            if (0 <= A <= 1) and (0 <= B <= 1) :
                valorA.insert(i, A)
                valorB.insert(i, B)
            else:
                print("Digitos inválidos\n")
                i = i - 1
        except ValueError:
            print("Por favor, digite apenas entre 1 e 0\n")
    
    Colunas['A'] = valorA
    Colunas['B'] = valorB
    
    print("\nTabela Verdade Disjunção\n")
    CriaTabelaDin(Colunas, "V", 2)

# Função para Calcular Operação de Conjunção
def CalculadoraConjuncao(): 
    Colunas = pd.DataFrame({'A': [], 'B': []}) 
    valorA = []
    valorB = []
    i = 0
    while i < 4 : 
        try:
            A = int(input(f"Insira um valor entre 0 e 1 para o {i+1}° A: "))
            B = int(input(f"Insira um valor entre 0 e 1 para o {i+1}° B: "))
            i = i + 1
            if (0 <= A <= 1) and (0 <= B <= 1) :
                valorA.insert(i, A)
                valorB.insert(i, B)
            else:
                print("Digitos inválidos\n")
                i = i - 1
        except ValueError:
            print("Por favor, digite apenas entre 1 e 0")
            
    Colunas['A'] = valorA
    Colunas['B'] = valorB
    
    print("\nTabela Verdade Conjunção\n")
    CriaTabelaDin(Colunas, "∧", 2)

# Função para Calcular Operação Condicional    
def CalculadoraCondicional():
    Colunas = pd.DataFrame({'A': [], 'B': []}) 
    valorA = []
    valorB = []
    i = 0
    while i < 4 : 
        try:
            A = int(input(f"Insira um valor entre 0 e 1 para o {i+1}° A: "))
            B = int(input(f"Insira um valor entre 0 e 1 para o {i+1}° B: "))
            i = i + 1
            if (0 <= A <= 1) and (0 <= B <= 1) :
                valorA.insert(i, A)
                valorB.insert(i, B)
            else:
                print("Digitos inválidos\n")
                i = i - 1
        except ValueError:
            print("Por favor, digite apenas entre 1 e 0")
            
    Colunas['A'] = valorA
    Colunas['B'] = valorB
    
    print("\nTabela Verdade Condicional\n")
    CriaTabelaDin(Colunas, "⭢", 2)

# Função para Calcular Operação Bicondicional    
def CalculadoraBicondicional():
    Colunas = pd.DataFrame({'A': [], 'B': []}) 
    valorA = []
    valorB = []
    i = 0
    while i < 4 : 
        try:
            A = int(input(f"Insira um valor entre 0 e 1 para o {i+1}° A: "))
            B = int(input(f"Insira um valor entre 0 e 1 para o {i+1}° B: "))
            i = i + 1
            if (0 <= A <= 1) and (0 <= B <= 1) :
                valorA.insert(i, A)
                valorB.insert(i, B)
            else:
                print("Digitos inválidos\n")
                i = i - 1
        except ValueError:
            print("Por favor, digite apenas entre 1 e 0")
            
    Colunas['A'] = valorA
    Colunas['B'] = valorB
    
    print("\nTabela Verdade Bicondicional\n")
    CriaTabelaDin(Colunas, "↔", 2)

# Função para Calcular Operação de Negação
def CalculadoraNegacao():
    Colunas = pd.DataFrame({'A': []}) 
    valorA = []
    i = 0
    while i < 2 : 
        try:
            A = int(input(f"Insira um valor entre 0 e 1 para o {i+1}° A: "))
            i = i + 1
            if (0 <= A <= 1):
                valorA.insert(i, A)
            else:
                print("Digitos inválidos\n")
                i = i - 1
        except ValueError:
            print("Por favor, digite apenas entre 1 e 0")
            
    Colunas['A'] = valorA
    
    print("\nTabela Verdade Negação\n")
    CriaTabelaDin(Colunas, "¬", 1)
    
# Função para criação da tabela
def CriaTabela(nome_tabela, col = 0): 
    nome_table = nome_tabela
    
    if col == 2: 
        df = pd.DataFrame({'A': [], 'B': []}) # Cria uma tabela com coluna A B
        InserirValores(df, nome_table, col = 2) 
        Tabela = InserirValores(df, nome_table, col = 2) # Passa a tabela e um parametro com o valor lógico desejado e recebe uma tabela pronta
        print(tabulate(Tabela, headers='keys', tablefmt= 'rounded_grid', showindex= False)) # rounded_grid double_grid
    elif col == 1:
        df = pd.DataFrame({'A': []}) # Cria uma tabela com coluna A
        InserirValores(df, nome_table, col = 1) # Passa a tabela e um parametro com o valor lógico desejado
        Tabela = InserirValores(df, nome_table, col = 1) # Passa a tabela e um parametro com o valor lógico desejado e recebe uma tabela pronta
        print(tabulate(Tabela, headers='keys', tablefmt='rounded_grid', showindex= False))

# Função para criação da tabela dinâmica       
def CriaTabelaDin(nome_tabela, operacao ,col = 0): 
    if col == 2: 
        Tabela = InserirValoresDin(nome_tabela, operacao, col = 2) # Passa a tabela e um parametro com o valor lógico desejado e recebe uma tabela pronta
        print(tabulate(Tabela, headers='keys', tablefmt= 'rounded_grid', showindex= False)) # rounded_grid double_grid
    elif col == 1:
        Tabela = InserirValoresDin(nome_tabela, operacao, col = 1) # Passa a tabela e um parametro com o valor lógico desejado e recebe uma tabela pronta
        print(tabulate(Tabela, headers='keys', tablefmt='rounded_grid', showindex= False))
        
# Função para inserir valores em uma tabela    
def InserirValores(tabela, operacao, col = 0):
    if col == 2:
        
        resultado = pd.concat([Col2, tabela], axis= 0) # Cria uma tabela juntando a tabela passada por parametro e a tabela com valores pré definidos de padrões de operações lógicas com 1 e 0
        cont = len(resultado)
        
        if operacao == 'V':
            valor = []
            for i in range(cont) : # Realiza verificação dos indices da tabela e realiza a operação guardando o resultado 
                indA = resultado.at[i, 'A']
                indB = resultado.at[i, 'B']
                if (indA == 0 and indB == 0):
                    valor.insert(i, 0)
                else:
                    valor.insert(i, 1)
        
            # Cria um Dic com chaves e valores recebidos do loop
            ResultOperacao = {'A V B' : []}
            ResultOperacao['A V B'] = valor
            
            # Adiciona a coluna de resultado na tabela formada nesta função e retorna a tabela completa com operações e resultados        
            ColResul = pd.DataFrame(ResultOperacao)
            TabelaFinal = pd.concat([resultado, ColResul], axis= 1) 
            TabelaFormatada = TabelaFinal.astype(int)
            return TabelaFormatada 
            
        elif operacao == '∧':
            valor = []
            for i in range(cont):
                indA = resultado.at[i, 'A']
                indB = resultado.at[i, 'B']
                if (indA == 1 and indB == 1):
                    valor.insert(i, 1)
                else:
                    valor.insert(i, 0)
            
            # Cria um Dic com chaves e valores recebidos do loop
            ResultOperacao = {'A ∧ B' : []}
            ResultOperacao['A ∧ B'] = valor
                    
            # Adiciona a coluna de resultado na tabela formada nesta função e retorna a tabela completa com operações e resultados        
            ColResul = pd.DataFrame(ResultOperacao)
            TabelaFinal = pd.concat([resultado, ColResul], axis= 1) 
            TabelaFormatada = TabelaFinal.astype(int) 
            return TabelaFormatada 
        
        elif operacao == '⭢':
            valor = []
            for i in range(cont):
                indA = resultado.at[i, 'A']
                indB = resultado.at[i, 'B']
                if (indA == 1 and indB == 0):
                    valor.insert(i, 0)
                else:
                    valor.insert(i, 1)
            
            # Cria um Dic com chaves e valores recebidos do loop
            ResultOperacao = {'A ⭢ B' : []}
            ResultOperacao['A ⭢ B'] = valor
                    
            # Adiciona a coluna de resultado na tabela formada nesta função e retorna a tabela completa com operações e resultados        
            ColResul = pd.DataFrame(ResultOperacao)
            TabelaFinal = pd.concat([resultado, ColResul], axis= 1) 
            TabelaFormatada = TabelaFinal.astype(int) 
            return TabelaFormatada
        
        elif operacao == '↔':
            valor = []
            for i in range(cont):
                indA = resultado.at[i, 'A']
                indB = resultado.at[i, 'B']
                if (indA == indB):
                    valor.insert(i, 1)
                else:
                    valor.insert(i, 0)
            
            # Cria um Dic com chaves e valores recebidos do loop
            ResultOperacao = {'A ↔ B' : []}
            ResultOperacao['A ↔ B'] = valor
                    
            # Adiciona a coluna de resultado na tabela formada nesta função e retorna a tabela completa com operações e resultados        
            ColResul = pd.DataFrame(ResultOperacao)
            TabelaFinal = pd.concat([resultado, ColResul], axis= 1) 
            TabelaFormatada = TabelaFinal.astype(int) 
            return TabelaFormatada
        
    elif col == 1:
        
        resultado = pd.concat([Col1, tabela], axis= 0) # Cria uma tabela juntando a tabela passada por parametro e a tabela com valores pré definidos de padrões de operações lógicas com 1 e 0
        cont = len(resultado)  
        if operacao == '¬':
            valor = []
            for i in range(cont):
                indA = resultado.at[i, 'A']
                if indA == 1:
                    valor.insert(i, 0)
                else:
                    valor.insert(i, 1)
                    
            # Cria um Dic com chaves e valores recebidos do loop
            ResultOperacao = {'¬ A' : []}
            ResultOperacao['¬ A'] = valor
                    
            # Adiciona a coluna de resultado na tabela formada nesta função e retorna a tabela completa com operações e resultados        
            ColResul = pd.DataFrame(ResultOperacao)
            TabelaFinal = pd.concat([resultado, ColResul], axis= 1) 
            TabelaFormatada = TabelaFinal.astype(int) 
            return TabelaFormatada 
    
    else:
        return print("Nenhuma tabela foi fornecida!")             

# Função para inserir valores em uma tabela dinâmica    
def InserirValoresDin(tabela, operacao, col = 0):
    if col == 2:
        
        if operacao == 'V':
            cont = len(tabela)
            valor = []
            for i in range(cont) : # Realiza verificação dos indices da tabela e realiza a operação guardando o resultado 
                indA = tabela.at[i, 'A']
                indB = tabela.at[i, 'B']
                if (indA == 0 and indB == 0):
                    valor.insert(i, 0)
                else:
                    valor.insert(i, 1)
                    
        # Cria um Dic com chaves e valores recebidos do loop
            ResultOperacao = {'A V B' : []}
            ResultOperacao['A V B'] = valor
            
            # Adiciona a coluna de resultado na tabela formada nesta função e retorna a tabela completa com operações e resultados        
            ColResul = pd.DataFrame(ResultOperacao)
            TabelaFinal = pd.concat([tabela, ColResul], axis= 1) 
            return TabelaFinal 
        
        if operacao == '∧':
                cont = len(tabela)
                valor = []
                for i in range(cont) :  
                    indA = tabela.at[i, 'A']
                    indB = tabela.at[i, 'B']
                    if (indA == 1 and indB == 1):
                        valor.insert(i, 1)
                    else:
                        valor.insert(i, 0)
                        
            # Cria um Dic com chaves e valores recebidos do loop
                ResultOperacao = {'A ∧ B' : []}
                ResultOperacao['A ∧ B'] = valor
                
                # Adiciona a coluna de resultado na tabela formada nesta função e retorna a tabela completa com operações e resultados        
                ColResul = pd.DataFrame(ResultOperacao)
                TabelaFinal = pd.concat([tabela, ColResul], axis= 1) 
                return TabelaFinal 
            
        elif operacao == '⭢':
            cont = len(tabela)
            valor = []
            for i in range(cont):
                indA = tabela.at[i, 'A']
                indB = tabela.at[i, 'B']
                if (indA == 1 and indB == 0):
                    valor.insert(i, 0)
                else:
                    valor.insert(i, 1)
            
            # Cria um Dic com chaves e valores recebidos do loop
            ResultOperacao = {'A ⭢ B' : []}
            ResultOperacao['A ⭢ B'] = valor
                    
            # Adiciona a coluna de resultado na tabela formada nesta função e retorna a tabela completa com operações e resultados        
            ColResul = pd.DataFrame(ResultOperacao)
            TabelaFinal = pd.concat([tabela, ColResul], axis= 1) 
            return TabelaFinal
        
        elif operacao == '↔':
            cont = len(tabela)
            valor = []
            for i in range(cont):
                indA = tabela.at[i, 'A']
                indB = tabela.at[i, 'B']
                if (indA == indB):
                    valor.insert(i, 1)
                else:
                    valor.insert(i, 0)
            
            # Cria um Dic com chaves e valores recebidos do loop
            ResultOperacao = {'A ↔ B' : []}
            ResultOperacao['A ↔ B'] = valor
                    
            # Adiciona a coluna de resultado na tabela formada nesta função e retorna a tabela completa com operações e resultados        
            ColResul = pd.DataFrame(ResultOperacao)
            TabelaFinal = pd.concat([tabela, ColResul], axis= 1) 
            return TabelaFinal    
    
    elif col == 1:
        if operacao == '¬':
            cont = len(tabela)
            valor = []
            for i in range(cont):
                indA = tabela.at[i, 'A']
                if indA == 1:
                    valor.insert(i, 0)
                else:
                    valor.insert(i, 1)
                    
            # Cria um Dic com chaves e valores recebidos do loop
            ResultOperacao = {'¬A' : []}
            ResultOperacao['¬A'] = valor
                    
            # Adiciona a coluna de resultado na tabela formada nesta função e retorna a tabela completa com operações e resultados        
            ColResul = pd.DataFrame(ResultOperacao)
            TabelaFinal = pd.concat([tabela, ColResul], axis= 1) 
            return TabelaFinal    
        
    else:
        return print("Nenhuma tabela foi fornecida!")

# Execução do código
Menu() 
