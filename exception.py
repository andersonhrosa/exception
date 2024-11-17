import datetime

def calcular_idade():
    while True:
        nome_completo = input("Digite seu nome completo: ")
        ano_nascimento_str = input("Digite seu ano de nascimento (entre 1922 e 2021): ")

        try:
            ano_nascimento = int(ano_nascimento_str)
            if 1922 <= ano_nascimento <= 2021:
                ano_atual = datetime.datetime.now().year
                idade = ano_atual - ano_nascimento
                print(f"{nome_completo} completará {idade} anos em 2022.")
                break
            else:
                print("Ano de nascimento inválido. Digite um ano entre 1922 e 2021.")
        except ValueError:
            print("Você não digitou um número válido para o ano de nascimento.")

calcular_idade()
