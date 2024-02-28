# jogo.py
from perguntas import perguntas

def exibir_pergunta(pergunta):
    print(pergunta["pergunta"])
    for opcao in pergunta["opcoes"]:
        print(opcao)
    resposta_jogador = input("Escolha a opção correta (a, b, c ou d): ").lower()
    return resposta_jogador

def jogar():
    dinheiro_acumulado = 0

    for pergunta in perguntas:
        resposta_jogador = exibir_pergunta(pergunta)
        
        if resposta_jogador == pergunta["resposta"]:
            print("Resposta correta!\n")
            dinheiro_acumulado += 1000  
        else:
            print(f"Resposta incorreta! Sua pontuação final é: {dinheiro_acumulado}.\n")
            return

    print(f"Parabéns! Você acertou todas as perguntas. Sua pontuação final é: {dinheiro_acumulado}.\n")


if __name__ == "__main__":
    print("Bem-vindo ao Quem Quer Ser um Milionário?\nDeseja Jogar ?")
    resposta = input('Escolha: "s" ou "n"\n')
    
    if resposta == 's':
        jogar()
    else:
        print("Até a Próxima!!!")
    