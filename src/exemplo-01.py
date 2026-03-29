def ex01():
    print("\n")
    print("🟢 Bem vindo ao programa que imprime a mensagem na tela!")
    
    nome = input("Por favor, digite seu nome: ")
    
    print(f"Olá, {nome}!")

def exe01():
    print("\n")
    print("🟢 Bem vindo ao programa que conta a quantidade de caracteres na mensagem!")

    nome = input("Por favor, digite seu nome: ")
    
    len_nome = len(nome)

    print(f"O seu nome possui {len_nome} caracteres")

def exe02():
    print("\n")
    print("🟢 Bem vindo ao programa que soma dois valores!")

    def ler_inteiro(prompt):
        while True:
            valor = input(prompt)
            try:
                return int(valor)
            except ValueError:
                print("Valor inválido! Digite um número inteiro.")

    n1 = ler_inteiro("Digite o primeiro valor: ")
    n2 = ler_inteiro("Digite o segundo valor: ")
    
    soma = n1 + n2

    print(f"A soma dos dois valores é: {soma}")

programas = {
    "1": ex01,
    "2": exe01,
    "3": exe02
}

def menu():
    print("Digite o número do que quer executar:")
    print("1 - Exemplo 01")
    print("2 - Exercício 01")
    print("3 - Exercício 02")
    print("0 - Sair")

while True:
    menu()
    escolha = input("> ").strip()

    if escolha == "0":
        print("Tchau!")
        break

    func = programas.get(escolha)

    if func:
        func()
        break
    else:
        print("Opção inválida, tente novamente!")