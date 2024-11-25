import os
import platform

def limpar_tela():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def funcao_menu():
    while True:
        limpar_tela()

        print("\t\t# PALAVRAS PALÍNDROMAS #\n")
        print("\t0 - Sair do programa.")
        print("\t1 - O que são palavras palíndromas?")
        print("\t2 - Testar se uma palavra é palíndroma.")
        opcao = input("\n\tDigite a opção desejada:")
        
        if opcao.isdigit():
            return int(opcao)
        else: 
            print("\n\tDados inválidos!\n\tPressione qualquer tecla para voltar ao menu...")
            input()
    

def palindroma(palavra):
    inicio = 0 
    fim = len(palavra) - 1

    while inicio < fim:
        if palavra[inicio].lower() != palavra[fim].lower():
            return False
        inicio += 1
        fim -=1
    return True

def executar_prog():
    while True:

        limpar_tela()
        menu = funcao_menu()

        match menu:
            case 0:
                break
            case 1:
                print("\n\tPalavras palíndromas são palavras que podem ser lidas da mesma maneira tanto de \n\ttrás para frente quanto de frente para trás, como 'arara', 'radar' ou 'esse'")
            case 2:
                palavra = input("\n\tDigite uma palavra:")
                resultado = palindroma(palavra)

                if resultado:
                    print(f"\n\tA palavra '{palavra}' é palíndroma!")
                else:
                    print(f"\n\tA palavra '{palavra}' não é palíndroma!")
            case _:
                print("\n\tDados inválidos!")
                
        print("\tPressione qualquer tecla para voltar ao menu...")
        input()

# PROGRAMA PRINCIPAL #
executar_prog()