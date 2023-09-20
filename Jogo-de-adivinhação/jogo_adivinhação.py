
import random #biblioteca para gerar numeros aleatorios


def main():

    print("Bem-vindo ao Jogo de Adivinhação!") #interação com o usuario
    usuario = input("Informe seu Nome:")
    print("Estou pensando em um número entre 1 e 100. Tente adivinhar se for capaz!!!") #interação com o usuario
    numero_secreto = random.randint(1, 100)  #utilizando a biblioteca para gerar um numero aleatório
    tentativas = 0  #o numero de tentativas inicio com o valor 0

    while True: #utilizar a estrutura de repetição while para quando o valor logico ainda for verdadeiro
        try:
            palpite = int(input("Digite o seu palpite: ")) #interação com o usuario, para que o usuario chute um numero
            tentativas += 1 # acrescenta valor ao numero de tentativas

            if palpite < numero_secreto: #utilizei uma estrutura de condição para avaliar se o palpite do usuario foi menor que o numero aleatorio gerado
                print(usuario , ",Tente um número maior.")
            elif palpite > numero_secreto: #utilizei uma estrutura de condição para avaliar se o palpite do usuario foi maior que o numero aleatorio gerado
                print(usuario , ",Tente um número menor.")
            else: # se não o usuario conseguiu chegar ao valor certo
                print("Parabéns!" , usuario , f",Você acertou em {tentativas} tentativas.")
                break
        except ValueError: #caso não consiga gerar o codigo, irá mostrar a mensagem parar inserir um número valido
            print("Por favor" , usuario , "digite um número válido.")

if __name__ == "__main__":
    main()