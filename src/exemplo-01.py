# Seleção do programa
programa = input(
    "Digite o número do que quer executar: \n" +
    "\n" +
    "1 - Exemplo 01 \n" +
    "2 - Exercício 01 \n" +
    "3 - Exercício 02 \n"
)

if programa == '1':
    # Exemplo 01 - Imprimindo uma mensagem na tela
    
    print("\n")
    print("🟢 Bem vindo ao programa que imprime a mensagem na tela!")
    
    nome = input("Por favor, digite seu nome: ")
    
    print(f"Olá, {nome}!")

elif programa == '2':
    # Exercício 1 - Crie um programa que o usuário digita o seu nome e retorna o número de caracteres
    
    print("\n")
    print("🟢 Bem vindo ao programa que conta a quantidade de caracteres na mensagem!")

    nome = input("Por favor, digite seu nome: ")
    
    len_nome = len(nome)

    print(f"O seu nome possui {len_nome} caracteres")

elif programa == '3':
    # Exercício 2 - Programa que some dois valores que o usuário inseriu
    
    print("\n")
    print("🟢 Bem vindo ao programa que soma dois valores!")

    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))
    
    soma = n1 + n2

    print(f"A soma dos dois valores é: {soma}")